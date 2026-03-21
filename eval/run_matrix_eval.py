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
from langchain_ollama import OllamaEmbeddings
from langchain_community.llms import Ollama

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
EMBEDDING_MODELS = ["mxbai-embed-large", "qllama/multilingual-e5-large", "qwen3-embedding"]
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

async def run_evaluation(limit: int = 0):
    print("═══ ORQUESTADOR DE EVALUACIÓN DE MATRIZ ═══")
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Carga de Preguntas
    df = load_questions()
    if limit > 0:
        df = df.head(limit)
    print(f"Cargadas {len(df)} preguntas para evaluación.")

    output_file = RESULTS_DIR / "eval_results_matrix.jsonl"
    print(f"Resultados se guardarán en: {output_file}")

    # 2. Inicializar Métricas (Juez Único)
    print(f"Inicializando métricas con Juez: {JUDGE_MODEL}")
    faithfulness_metric = FaithfulnessMetric(provider="ollama", model_id=JUDGE_MODEL)
    relevance_metric = ContextRelevanceMetric(provider="ollama", model_id=JUDGE_MODEL)
    precision_metric = ContextPrecisionMetric(provider="ollama", model_id=JUDGE_MODEL)
    answer_rel_metric = AnswerRelevancyMetric(provider="ollama", model_id=JUDGE_MODEL)

    # 3. Bucles de la Matriz de Permutaciones
    for gen_model in GENERATORS:
        print(f"\n🚀 Iniciando Evaluación con Generador: [{gen_model.upper()}]")
        try:
            llm = Ollama(model=gen_model, base_url=settings.ollama_base_url)
        except Exception as e:
            print(f"❌ Error al cargar generador {gen_model}. Saltando... ({e})")
            continue

        for e_model in EMBEDDING_MODELS:
            print(f"  🔋 Procesando Embedding: [{e_model.upper()}]")
            try:
                embeddings = OllamaEmbeddings(model=e_model, base_url=settings.ollama_base_url)
                embeddings.embed_query("warmup")
            except Exception as e:
                print(f"  ❌ Embedding {e_model} no cargado. Saltando... ({e})")
                continue

            for c_strat in CHUNK_STRATEGIES:
                for db_motor in DB_MOTORS:
                    comb_id = f"{e_model.replace(':', '_')}_{c_strat}_{db_motor}"
                    print(f"    🗄 Evaluando: [{e_model} | {c_strat} | {db_motor}]")

                    try:
                        # 3.1 Cargar Vector Store
                        vector_store = get_vector_store(db_motor, e_model, c_strat, embeddings)
                        rag_engine = RAGEngine(vector_store=vector_store)
                        rag_chain = rag_engine.get_chain(llm)

                        # 3.2 Evaluar por pregunta
                        for _, row in df.iterrows():
                            q_id = row['id']
                            question = row['question']
                            print(f"      - Evaluando Q{q_id}...", end=" ", flush=True)

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

                            print(f"Fid: {result_data['faithfulness_score']} | Rel: {result_data['relevance_score']} | Prec: {result_data['context_precision_score']} | AnsRel: {result_data['answer_relevancy_score']}")

                    except Exception as e:
                        print(f"    ❌ Error procesando combinación {comb_id}: {str(e)}")

                    time.sleep(2) # Respiro para Ollama

    print(f"\n✅ Evaluación de Matriz Completada. Resultados en {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Correr Evaluación de la Matriz de Experimentos")
    parser.add_argument("--limit", type=int, default=0, help="Limitar número de preguntas (0 para todas)")
    args = parser.parse_args()
    
    asyncio.run(run_evaluation(limit=args.limit))
