import pandas as pd
import asyncio
import json
import time
from pathlib import Path
from src.agent.graph import AgentGraph

# Config
INPUT_FILE = Path("eval/question_bank_v1.csv")
OUTPUT_DIR = Path("eval/results/V2")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

async def run_v2_eval():
    print("🚀 Iniciando Evaluación V2 (Agente Autónomo)...")
    
    # Cargar Preguntas
    df = pd.read_csv(INPUT_FILE, dtype={'id': str})
    
    # Inicializar Agente
    agent = AgentGraph()
    
    results = []
    
    for idx, row in df.iterrows():
        q_id = row['id']
        question = row['question']
        print(f"[{idx+1}/{len(df)}] Procesando Q{q_id}...")
        
        start_time = time.time()
        try:
            # Ejecutar Agente
            state = await agent.app.ainvoke({"question": question})
            response = state.get("generation", "")
            final_faith = state.get("faithfulness_score", 0.0)
            retries = state.get("retry_count", 0)
            
            latency = time.time() - start_time
            
            # Guardar
            results.append({
                "question_id": q_id,
                "question": question,
                "response": response,
                "latency": latency,
                "faithfulness_score": final_faith,
                "retries": retries,
                "model": "Agente V2"
            })
            print(f"  -> Latency: {latency:.2f}s | Score: {final_faith} | Retries: {retries}")
            
        except Exception as e:
            print(f"  ❌ Error: {e}")
            results.append({
                "question_id": q_id,
                "question": question,
                "response": f"Error: {e}",
                "latency": 0,
                "error": str(e)
            })

    # Guardar Resultados
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    out_file = OUTPUT_DIR / f"eval_v2_{timestamp}.json"
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    print(f"\n✅ Evaluación V2 completada. Resultados en {out_file}")

if __name__ == "__main__":
    asyncio.run(run_v2_eval())
