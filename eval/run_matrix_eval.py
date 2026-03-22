"""
run_matrix_eval.py — Evaluador de Matriz de Rendimiento

Prueba múltiples combinaciones de Embeddings + Estrategia de Fragmentación +
DB Motor (FAISS/Qdrant) contra varios Generadores LLM (Ollama, Gemini, OpenRouter),
guardando latencias y puntuación de alucinación para auditoría matricial en `eval/results/Matrix`.

Uso:
    uv run python eval/run_matrix_eval.py [OPCIONES]

Opciones:
    --limit N             Limitar número de preguntas del banco a evaluar.
    --embedding EMB       Filtrar por un modelo de embedding específico (ej: mxbai-embed-large).
    --chunk-strategy CHK  Filtrar por estrategia de fragmentación (500, 1000, semantic).
    --db-motor DB         Filtrar por motor de base de datos (faiss, qdrant_local).
    --generator GEN       Filtrar por modelo de generación de respuesta (ej: qwen2.5:3b).
    --judge JUDGE         Definir el modelo LLM que actuará como juez evaluator (ej: llama3.1).
    --architecture ARCH   Filtrar por arquitectura RAG (v0, v1, v2).
    --overwrite           Sobrescribir resultados previos de las combinaciones evaluadas en lugar de acumular.
"""

import argparse
import asyncio
import time
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from langchain_community.vectorstores import FAISS
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from langchain_ollama import OllamaEmbeddings, OllamaLLM

import sys
# Asegurar que el directorio raíz esté en el PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.config.settings import settings
from src.chat.rag import RAGEngine
from src.metrics.faithfulness import FaithfulnessMetric
from src.metrics.context_relevance import ContextRelevanceMetric
from src.metrics.context_precision import ContextPrecisionMetric
from src.metrics.answer_relevancy import AnswerRelevancyMetric
from src.metrics.factscore import FactScoreMetric

# Directorios
INPUT_FILE = Path("eval/question_bank_v1.csv")
RESULTS_DIR = Path("eval/results/Matrix")
FAISS_DIR = Path("data/vector_matrix/faiss")
QDRANT_DIR = Path("data/vector_matrix/qdrant_local")

# Parámetros de la Matriz (Adaptables por el usuario)
EMBEDDING_MODELS = ["mxbai-embed-large", "nomic-embed-text-v2-moe", "qwen3-embedding"]
CHUNK_STRATEGIES = [500, 1000, "semantic"]
DB_MOTORS = ["faiss", "qdrant_local"]
GENERATORS = [
    "deepseek-r1:8b", "qwen3:8b", "gpt-oss:20b", 
    "gemini-3-flash-preview", "gemini-3.1-pro-preview", "gemini-3.1-flash-lite-preview"
]  # Modelos de generación de respuestas de la matriz
JUDGE_MODEL = "llama3.1"  # Único juez para todas las evaluaciones

def load_questions():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Banco de preguntas no encontrado en {INPUT_FILE}")
    return pd.read_csv(INPUT_FILE, dtype={'id': str})

def remove_existing_results(output_file, embedding_models, chunk_strategies, db_motors, generators, architectures):
    """Elimina del archivo JSONL las filas que coinciden con las combinaciones que se van a calcular."""
    import json
    if not output_file.exists():
        return
    rows = []
    with open(output_file, "r", encoding="utf-8") as f:
         for line in f:
             try:
                 row = json.loads(line.strip())
                 # Si coincide con TODO lo que vamos a calcular, lo ignoramos (borramos)
                 is_match = (
                     row.get("generator") in generators and
                     row.get("architecture") in architectures and
                     (row.get("embedding") in embedding_models or row.get("embedding") == "N/A") and
                     (row.get("chunk_strategy") in [str(c) for c in chunk_strategies] or row.get("chunk_strategy") == "N/A") and
                     (row.get("db_motor") in db_motors or row.get("db_motor") == "N/A")
                 )
                 if not is_match:
                     rows.append(row)
             except Exception:
                 continue
                 
    with open(output_file, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"🧹 Sobreescritura: Removidas {sum(1 for _ in open(output_file)) - len(rows) if output_file.exists() else 0} filas coincidentes del JSONL.")

def get_vector_store(db_motor: str, e_model: str, c_strat: str, embeddings):
    """Instancia el VectorStore correspondiente a partir de la matriz de metadatos."""
    comb_id = f"{e_model.replace(':', '_')}_{c_strat}_{db_motor}"
    
    if db_motor == "faiss":
        path = FAISS_DIR / comb_id
        if not path.exists():
            raise FileNotFoundError(f"Índice FAISS no encontrado para {comb_id}")
        return FAISS.load_local(str(path), embeddings, allow_dangerous_deserialization=True)
        
    elif db_motor == "qdrant_local":
        path = QDRANT_DIR / comb_id
        if not path.exists():
            raise FileNotFoundError(f"Base Qdrant no encontrada para {comb_id}")
        client = QdrantClient(path=str(path))
        collection_name = f"tfm_matrix_{comb_id.lower()}"
        if not client.collection_exists(collection_name):
            raise FileNotFoundError(f"Colección Qdrant no encontrada: {collection_name}")
        return QdrantVectorStore(client=client, collection_name=collection_name, embedding=embeddings)
        
    else:
        raise ValueError(f"Motor DB '{db_motor}' no soportado.")

async def run_evaluation(args):
    print("=== ORQUESTADOR DE EVALUACIÓN DE MATRIZ ===")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Carga de Preguntas
    df = load_questions()
    if args.limit > 0:
        df = df.head(args.limit)
    print(f"Cargadas {len(df)} preguntas para evaluación.")

    output_file = RESULTS_DIR / "eval_results_matrix.jsonl"
    print(f"Resultados se guardarán en: {output_file}")

    # Filtrar parámetros de la matriz según argumentos
    embedding_models = [args.embedding] if args.embedding else EMBEDDING_MODELS
    chunk_strategies = [int(args.chunk_strategy) if args.chunk_strategy.isdigit() else args.chunk_strategy] if args.chunk_strategy else CHUNK_STRATEGIES
    db_motors = [args.db_motor] if args.db_motor else DB_MOTORS
    generators = [args.generator] if args.generator else GENERATORS
    judge_model = args.judge if args.judge else JUDGE_MODEL
    
    # 📝 FILTRO DE ARQUITECTURAS
    architectures = [args.architecture] if args.architecture else ["v0", "v1", "v2"]

    # --- SOBREESCRITURA SELECTIVA O RECUPERACIÓN (SKIP) ---
    executed_keys = set()
    if getattr(args, "overwrite", False) and output_file.exists():
        print("Tratando de sobreescribir combinaciones previas...")
        remove_existing_results(output_file, embedding_models, chunk_strategies, db_motors, generators, architectures)
    elif output_file.exists():
        print("Cargando combinaciones ya evaluadas para evitar duplicados...")
        with open(output_file, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line.strip())
                    key = (str(r.get("question_id")), r.get("architecture"), r.get("generator"), r.get("embedding"), str(r.get("chunk_strategy")), r.get("db_motor"))
                    executed_keys.add(key)
                except Exception:
                    pass
        print(f"Detectadas {len(executed_keys)} sub-pruebas ya calculadas. Se ignorarán.")
    for e in embedding_models:
        if e not in EMBEDDING_MODELS:
            print(f"⚠️ Alerta: '{e}' no está pre-configurado en EMBEDDING_MODELS.")
    for c in chunk_strategies:
        if c not in CHUNK_STRATEGIES:
            print(f"⚠️ Alerta: '{c}' no está pre-configurado en CHUNK_STRATEGIES.")

    # 2. Inicializar Métricas (Juez Único)
    print(f"Inicializando métricas con Juez: {judge_model}")
    faithfulness_metric = FaithfulnessMetric(provider="ollama", model_id=judge_model)
    relevance_metric = ContextRelevanceMetric(provider="ollama", model_id=judge_model)
    precision_metric = ContextPrecisionMetric(provider="ollama", model_id=judge_model)
    answer_rel_metric = AnswerRelevancyMetric(provider="ollama", model_id=judge_model)
    factscore_metric = FactScoreMetric(provider="ollama", model_id=judge_model)

    # 3. Bucles de la Matriz de Permutaciones
    for gen_model in generators:
        print(f"\n🚀 Iniciando Evaluación con Generador: [{gen_model.upper()}] | Juez: [{judge_model.upper()}]")
        try:
            if gen_model.startswith("gemini"):
                from src.core.providers.factory import ProviderFactory
                # Para Gemini, ProviderFactory se encarga.
                print(f"  ☁️ Cargando modelo Cloud Gemini: {gen_model}")
                llm = ProviderFactory.get_provider("gemini", gen_model)
            else:
                llm = OllamaLLM(model=gen_model, base_url=settings.ollama_base_url)
        except Exception as e:
            print(f"❌ Error al cargar generador {gen_model}. Saltando... ({e})")
            continue

        for e_model in embedding_models:
            print(f"  🔋 Procesando Embedding: [{e_model.upper()}]")
            try:
                embeddings = OllamaEmbeddings(model=e_model, base_url=settings.ollama_base_url)
                embeddings.embed_query("warmup")
            except Exception as e:
                print(f"  ❌ Embedding {e_model} no cargado. Saltando... ({e})")
                continue

            for c_strat in chunk_strategies:
                for db_motor in db_motors:
                    comb_id = f"{e_model.replace(':', '_')}_{c_strat}_{db_motor}"
                    print(f"    🗄 Evaluando Matriz Celda: [{e_model} | {c_strat} | {db_motor}]")

                    try:
                        # 3.1 Cargar Vector Store
                        vector_store = get_vector_store(db_motor, e_model, c_strat, embeddings)
                        rag_engine = RAGEngine(vector_store=vector_store)
                        rag_chain = rag_engine.get_chain(llm)

                        # 3.2 Evaluar por pregunta
                        for _, row in df.iterrows():
                            q_id = row['id']
                            question = row['question']

                            for arch in architectures:
                                # Evitar ejecuciones redundantes de v0 (No RAG) en cada combinación de matriz
                                if arch == "v0" and (e_model != embedding_models[0] or c_strat != chunk_strategies[0] or db_motor != db_motors[0]):
                                    continue

                                # --- SKIP DE COMBINACIONES YA CALCULADAS ---
                                match_e = e_model if arch != "v0" else "N/A"
                                match_c = str(c_strat) if arch != "v0" else "N/A"
                                match_db = db_motor if arch != "v0" else "N/A"
                                key = (str(q_id), arch, gen_model, match_e, match_c, match_db)
                                if key in executed_keys:
                                    continue

                                print(f"      - [Q{q_id}] Arch: {arch} | Gen: {gen_model} | Juez: {judge_model} | Emb: {e_model}...", end=" ", flush=True)

                                # Medir telemetría de recuperación
                                start_retrieval = time.time()
                                try:
                                    if arch == "v0":
                                        docs = []
                                    else:
                                        # Guardar recuperación para usar en métricas de v1/v2
                                        docs = rag_engine.retrieve_context(question)
                                    latency_retrieval = time.time() - start_retrieval
                                except Exception as e:
                                    docs = []
                                    latency_retrieval = 0.0
                                    print(f"[Error Retrieval: {e}]", end=" ")

                                # Medir telemetría de generación
                                start_gen = time.time()
                                try:
                                    if arch == "v0":
                                        raw_resp = llm.invoke(question)
                                        response = raw_resp.content if hasattr(raw_resp, 'content') else str(raw_resp)
                                    elif arch == "v1":
                                        raw_resp = rag_chain.invoke(question)
                                        response = raw_resp.content if hasattr(raw_resp, 'content') else str(raw_resp)
                                    elif arch == "v2":
                                        from src.agent.graph import AgentGraph
                                        is_gemini = gen_model.startswith("gemini")
                                        v2_provider = "gemini" if is_gemini else "ollama"
                                        agent = AgentGraph(provider=v2_provider, model_id=gen_model, force_local=not is_gemini, vector_store=vector_store)
                                        res_state = agent.app.invoke({"question": question})
                                        response = res_state.get("generation", "")
                                        if hasattr(response, 'content'):
                                             response = response.content
                                    latency_generation = time.time() - start_gen
                                except Exception as e:
                                    response = f"Error generación: {e}"
                                    latency_generation = 0.0

                                # 3.3 Calcular Métricas
                                faith_res = faithfulness_metric.evaluate(response, docs)
                                rel_res = relevance_metric.evaluate(question, docs)
                                prec_res = precision_metric.evaluate(question, docs)
                                ans_res = answer_rel_metric.evaluate(question, response)
                                fact_res = factscore_metric.calculate(response, docs)

                                # Simil de Costo en base a tiempo de GPU local ($1.50 USD por hora)
                                cost_est = ((latency_retrieval + latency_generation) / 3600.0) * 1.50

                            # Estructura del resultado
                                result_data = {
                                    "timestamp": datetime.now().isoformat(),
                                    "question_id": q_id,
                                    "question": question,
                                    "architecture": arch,
                                    "generator": gen_model,
                                    "embedding": e_model if arch != "v0" else "N/A",
                                    "chunk_strategy": str(c_strat) if arch != "v0" else "N/A",
                                    "db_motor": db_motor if arch != "v0" else "N/A",
                                    "response": response,
                                    "latency_retrieval_seg": latency_retrieval,
                                    "latency_generation_seg": latency_generation,
                                    "total_latency_seg": latency_retrieval + latency_generation,
                                    "cost_est": cost_est,
                                    "faithfulness_score": faith_res.get('score', 0.0),
                                    "faithfulness_reason": faith_res.get('reason', ""),
                                    "relevance_score": rel_res.get('score', 0.0),
                                    "relevance_reason": rel_res.get('reason', ""),
                                    "context_precision_score": prec_res.get('score', 0.0),
                                    "answer_relevancy_score": ans_res.get('score', 0.0),
                                    "factscore_score": fact_res.get('score', 0.0)
                                }

                            # Guardar incrementalmente en JSONL
                                with open(output_file, "a", encoding="utf-8") as f:
                                    f.write(json.dumps(result_data, ensure_ascii=False) + "\n")

                                print(f"Fid: {result_data['faithfulness_score']} | Rel: {result_data['relevance_score']} | Prec: {result_data['context_precision_score']} | AnRel: {result_data['answer_relevancy_score']} | Fact: {result_data['factscore_score']}")

                    except Exception as e:
                        print(f"    ❌ Error procesando combinación {comb_id}: {str(e)}")

                    finally:
                        # Liberar bloqueos de SQLite en local Qdrant
                        if db_motor == "qdrant_local" and 'vector_store' in locals():
                            try:
                                if hasattr(vector_store, "client") and hasattr(vector_store.client, "close"):
                                    vector_store.client.close()
                            except Exception:
                                pass

                    time.sleep(2) # Respiro para Ollama

    print(f"\n✅ Evaluación de Matriz Completada. Resultados en {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Correr Evaluación de la Matriz de Experimentos")
    parser.add_argument("--limit", type=int, default=0, help="Limitar número de preguntas (0 para todas)")
    parser.add_argument("--embedding", type=str, default="", help="Filtrar por modelo de embedding (ej: mxbai-embed-large)")
    parser.add_argument("--chunk-strategy", type=str, default="", help="Filtrar por estrategia chunking (500, 1000, semantic)")
    parser.add_argument("--db-motor", type=str, default="", help="Filtrar por db motor (faiss, qdrant_local)")
    parser.add_argument("--generator", type=str, default="", help="Filtrar por modelo generador (ej: qwen2.5:3b)")
    parser.add_argument("--judge", type=str, default="", help="Modelo usado como Juez evaluador (ej: llama3.1)")
    parser.add_argument("--architecture", type=str, choices=["v0", "v1", "v2"], default="", help="Filtrar por arquitectura (v0, v1, v2)")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescribir resultados de estas combinaciones en lugar de acumular")
    args = parser.parse_args()
    
    asyncio.run(run_evaluation(args))
