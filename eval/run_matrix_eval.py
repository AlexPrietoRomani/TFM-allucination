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

# Directorios
INPUT_FILE = Path("eval/question_bank_v1.csv")
RESULTS_DIR = Path("eval/results/Matrix")
FAISS_DIR = Path("data/vector_matrix/faiss")
QDRANT_DIR = Path("data/vector_matrix/qdrant_local")

# Parámetros de la Matriz (Adaptables por el usuario)
EMBEDDING_MODELS = ["mxbai-embed-large", "nomic-embed-text-v2-moe", "qwen3-embedding"]
CHUNK_STRATEGIES = [500, 1000, "semantic"]
DB_MOTORS = ["faiss", "qdrant_local"]
GENERATORS = ["qwen2.5:3b", "deepseek-r1:8b"]  # Modelos de generación de respuestas
JUDGE_MODEL = "llama3.1"  # Único juez para todas las evaluaciones

def load_questions():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Banco de preguntas no encontrado en {INPUT_FILE}")
    return pd.read_csv(INPUT_FILE, dtype={'id': str})

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
    print("═══ ORQUESTADOR DE EVALUACIÓN DE MATRIZ ═══")
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

    # Validación de parámetros introducidos por el usuario
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

    # 3. Bucles de la Matriz de Permutaciones
    for gen_model in generators:
        print(f"\n🚀 Iniciando Evaluación con Generador: [{gen_model.upper()}] | Juez: [{judge_model.upper()}]")
        try:
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
                            print(f"      - [Q{q_id}] Gen: {gen_model} | Juez: {judge_model} | Emb: {e_model} | Chunk: {c_strat} | DB: {db_motor}...", end=" ", flush=True)

                            # Medir telemetría de recuperación
                            start_retrieval = time.time()
                            try:
                                docs = rag_engine.retrieve_context(question)
                                latency_retrieval = time.time() - start_retrieval
                            except Exception as e:
                                docs = []
                                latency_retrieval = 0.0
                                print(f"[Error Retrieval: {e}]", end=" ")

                            # Medir telemetría de generación
                            start_gen = time.time()
                            try:
                                response = rag_chain.invoke(question)
                                latency_generation = time.time() - start_gen
                            except Exception as e:
                                response = f"Error generación: {e}"
                                latency_generation = 0.0

                            # 3.3 Calcular Métricas
                            faith_res = faithfulness_metric.evaluate(response, docs)
                            rel_res = relevance_metric.evaluate(question, docs)
                            prec_res = precision_metric.evaluate(question, docs)
                            ans_res = answer_rel_metric.evaluate(question, response)

                            # Costo estático (Ollama es gratis, 1M tokens gemini se puede proyectar)
                            cost_est = 0.0 # Ollama = 0

                            # Estructura del resultado
                            result_data = {
                                "timestamp": datetime.now().isoformat(),
                                "question_id": q_id,
                                "question": question,
                                "generator": gen_model,
                                "embedding": e_model,
                                "chunk_strategy": str(c_strat),
                                "db_motor": db_motor,
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
                                "answer_relevancy_score": ans_res.get('score', 0.0)
                            }

                            # Guardar incrementalmente en JSONL
                            with open(output_file, "a", encoding="utf-8") as f:
                                f.write(json.dumps(result_data, ensure_ascii=False) + "\n")

                            print(f"Fid: {result_data['faithfulness_score']} | Rel: {result_data['relevance_score']} | Prec: {result_data['context_precision_score']}")

                    except Exception as e:
                        print(f"    ❌ Error procesando combinación {comb_id}: {str(e)}")

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
    args = parser.parse_args()
    
    asyncio.run(run_evaluation(args))
