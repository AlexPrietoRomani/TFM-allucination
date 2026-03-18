import pandas as pd
import asyncio
import json
import time
from pathlib import Path
from src.agent.graph import AgentGraph

import argparse

# Config
INPUT_FILE = Path("eval/question_bank_v1.csv")
OUTPUT_DIR = Path("eval/results/V2")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

async def run_v2_eval(provider: str, model: str, limit: int = None):
    print(f"🚀 Iniciando Evaluación V2 (Agente Autónomo) con {provider}/{model}...")
    
    # Cargar Preguntas
    df = pd.read_csv(INPUT_FILE, dtype={'id': str})
    if limit:
        print(f"Limiting to first {limit} questions.")
        df = df.head(limit)
    
    agent = AgentGraph(provider=provider, model_id=model, force_local=True)
    
    results = []
    
    for idx, row in df.iterrows():
        print(f"[{idx+1}/{len(df)}] Procesando Q{row['id']}...", end=" ", flush=True)
        res = await evaluate_row_v2(row, agent)
        results.append(res)
        print(f"  -> Latency: {res['latency']:.2f}s | Score: {res.get('faithfulness_score', 0)}")

    # Guardar Resultados
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    out_file = OUTPUT_DIR / f"eval_v2_{timestamp}.json"
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    print(f"\n✅ Evaluación V2 completada. Resultados en {out_file}")

async def evaluate_row_v2(row, agent):
    q_id = str(row['id'])
    question = row['question']
    
    start_time = time.time()
    try:
        # Ejecutar Agente
        # Usamos context manager para timeout si fuera necesario, o simple await
        state = await agent.app.ainvoke({"question": question})
        response = state.get("generation", "")
        final_faith = state.get("faithfulness_score", 0.0)
        retries = state.get("retry_count", 0)
        
        latency = time.time() - start_time
        
        return {
            "question_id": q_id,
            "question": question,
            "response": response,
            "latency": latency,
            "faithfulness_score": final_faith,
            "retries": retries,
            "model": "Agente V2"
        }
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return {
            "question_id": q_id,
            "question": question,
            "response": f"Error: {e}",
            "latency": 0,
            "error": str(e)
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate Application V2")
    parser.add_argument("--provider", type=str, default="gemini", help="LLM Provider (gemini, ollama, etc)")
    parser.add_argument("--model", type=str, default="gemini-3-flash-preview", help="Model name")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of questions to process")
    
    args = parser.parse_args()
    asyncio.run(run_v2_eval(provider=args.provider, model=args.model, limit=args.limit))
