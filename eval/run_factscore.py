"""
run_factscore.py — Evaluador de Hechos Atómicos (FactScore)

Calcula la fidelidad de las respuestas generadas por el motor RAG
descomponiendo las oraciones en afirmaciones atómicas discretas (`FactScoreMetric`)
y verificando su apoyo en los documentos recuperados.

Uso:
    uv run python eval/run_factscore.py
"""

import pandas as pd
import asyncio
from pathlib import Path
from src.core.providers.factory import ProviderFactory
from src.chat.rag import RAGEngine
from src.metrics.factscore import FactScoreMetric

INPUT_FILE = Path("eval/question_bank_v1.csv")
RESULTS_DIR = Path("eval/results/Metrics")

async def run_factscore_eval():
    print("Iniciando Evaluación FactScore (Hechos Atómicos) con Ollama...")
    
    # Cargar y filtrar preguntas (Ej: Q2-Q4 para prueba rápida)
    df = pd.read_csv(INPUT_FILE, dtype={'id': str})
    df = df.iloc[1:4] # Q2, Q3, Q4
    
    # Inicializar componentes
    llm = ProviderFactory.get_provider("ollama", "gpt-oss:20b")
    rag_engine = RAGEngine()
    factscore = FactScoreMetric()
    
    results = []
    
    try:
        for idx, row in df.iterrows():
            q_id = row['id']
            question = row['question']
            
            print(f"\n[{idx+1}/{len(df)}] Procesando Q{q_id}...")
            
            # 1. RAG
            docs = rag_engine.retrieve_context(question)
            rag_chain = rag_engine.get_chain(llm)
            response = rag_chain.invoke(question)
            
            # 2. FactScore
            fs_result = factscore.calculate(response, docs)
            
            print(f"  -> Score: {fs_result.get('score', 0.0):.2f} ({fs_result.get('supported_claims', 0)}/{fs_result.get('total_claims', 0)})")
            
            # Guardar result aplanado
            results.append({
                "question_id": q_id,
                "question": question,
                "response": response,
                "factscore": fs_result.get("score", 0.0),
                "total_claims": fs_result.get("total_claims", 0),
                "supported": fs_result.get("supported_claims", 0),
                # Guardamos el desglose como string JSON para análisis posterior si se quiere
                "breakdown_json": str(fs_result.get("breakdown", [])) 
            })

        # Guardar CSV
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        df_res = pd.DataFrame(results)
        out_path = RESULTS_DIR / "factscore_eval.csv"
        df_res.to_csv(out_path, index=False)
        print(f"\nResultados FactScore guardados en: {out_path}")
        
    finally:
        from src.core.providers.ollama import OllamaProvider
        OllamaProvider.unload_model("gpt-oss:20b")

if __name__ == "__main__":
    asyncio.run(run_factscore_eval())
