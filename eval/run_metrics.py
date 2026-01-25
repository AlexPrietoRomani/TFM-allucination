import pandas as pd
import asyncio
from pathlib import Path
from src.metrics.faithfulness import FaithfulnessMetric
from src.metrics.context_relevance import ContextRelevanceMetric
# We need to retrieve the context again or store it during run_eval. 
# Since run_eval didn't store the full context objects in parquet/csv (it's hard to serialize list of objects clearly in flat csv),
# we ideally should modify run_eval to store 'retrieved_context_str' or similar.
# BUT, for Hito 10 without breaking everything, let's re-retrieve or assume we only have answer.
# Wait, 'Faithfulness' NEEDS context.
# We must modify 'src/chat/rag.py' to allow returning source docs AND answer, 
# and 'run_eval.py' to save those docs text.

# Plan B: Since we didn't save context text in run_eval.py output (only response), 
# we can't run metrics offline easily without re-running retrieval.
# So, this script will:
# 1. Load the Question Bank.
# 2. Re-run RAG (generate answer + docs).
# 3. Score immediately.
# This essentially replaces run_eval.py for the "Metrics" run.

from src.core.providers.factory import ProviderFactory
from src.chat.rag import RAGEngine
from src.core.config.settings import settings

INPUT_FILE = Path("eval/question_bank_v1.csv")
RESULTS_DIR = Path("eval/results/Metrics")

async def run_metrics_eval():
    print("Iniciando Evaluación de Métricas (Fidelidad & Relevancia) con Ollama...")
    
    # Cargar Preguntas
    df = pd.read_csv(INPUT_FILE, dtype={'id': str})
    
    # Filtrar preguntas 2 a 4 
    df = df.iloc[2:4]
    
    print(f"Preguntas seleccionadas: {df['id'].tolist()}")
    
    # Inicializar componentes
    # Usando Ollama para generación también para evitar límites de API
    llm = ProviderFactory.get_provider("ollama", "gpt-oss:20b")
    rag_engine = RAGEngine()
    
    # Inicializar Métricas
    faithfulness = FaithfulnessMetric()
    relevance = ContextRelevanceMetric()
    
    results = []
    
    try:
        print(f"Evaluando {len(df)} preguntas...")
        
        for idx, row in df.iterrows():
            question = row['question']
            q_id = row['id']
            
            print(f"[{idx+1}/{len(df)}] Q{q_id}...", end=" ", flush=True)
            
            # 1. RAG Recuperar & Generar
            docs = rag_engine.retrieve_context(question)
            rag_chain = rag_engine.get_chain(llm)
            response = rag_chain.invoke(question) 
            
            # 2. Puntuar Relevancia de Contexto
            rel_result = relevance.evaluate(question, docs)
            
            # 3. Puntuar Fidelidad
            faith_result = faithfulness.evaluate(response, docs)
            
            print(f"Fidelidad: {faith_result['score']} | Relevancia: {rel_result['score']}")
            
            results.append({
                "question_id": q_id,
                "question": question,
                "response": response,
                "context_snippet": docs[0].page_content[:100] if docs else "Ninguno",
                "faithfulness_score": faith_result['score'],
                "faithfulness_reason": faith_result['reason'],
                "relevance_score": rel_result['score'],
                "relevance_reason": rel_result['reason']
            })

        # Guardar
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        df_res = pd.DataFrame(results)
        output_csv = RESULTS_DIR / "metrics_eval_ollama_subset.csv"
        df_res.to_csv(output_csv, index=False)
        print(f"Métricas guardadas en {output_csv}")
        
    finally:
        # Limpieza
        from src.core.providers.ollama import OllamaProvider
        OllamaProvider.unload_model("gpt-oss:20b")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_metrics_eval())
