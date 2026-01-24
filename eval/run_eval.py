import argparse
import asyncio
import pandas as pd
import time
import os
from pathlib import Path
from datetime import datetime
from src.core.providers.factory import ProviderFactory
from src.core.config.settings import settings

# Configuration
INPUT_FILE = Path("eval/question_bank_v1.csv")
RESULTS_DIR = Path("eval/results/V0")

def load_questions():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Question bank not found at {INPUT_FILE}")
    return pd.read_csv(INPUT_FILE)

async def run_evaluation(provider: str, model: str, variant: str, run_label: str = "default"):
    print(f"Starting evaluation {variant} with {provider}/{model}...")
    
    # 1. Load Data
    df = load_questions()
    print(f"Loaded {len(df)} questions.")
    
    # 2. Prepare Results storage
    results = []
    
    # 3. Initialize Engine
    try:
        llm = ProviderFactory.get_provider(provider, model)
        rag_engine = None
        if variant == "V1":
            from src.chat.rag import RAGEngine
            rag_engine = RAGEngine()
            rag_chain = rag_engine.get_chain(llm)
    except Exception as e:
        print(f"Failed to initialize engine: {e}")
        return

    # 4. Iterate
    for index, row in df.iterrows():
        q_id = row['id']
        question = row['question']
        
        print(f"[{index+1}/{len(df)}] Processing Q{q_id}...", end=" ", flush=True)
        
        start_time = time.time()
        try:
            if variant == "V0":
                # Baseline
                response = llm.invoke(question)
                content = response.content
            else:
                # RAG V1
                content = rag_chain.invoke(question)
            
            error = None
        except Exception as e:
            content = ""
            error = str(e)
            print(f"Error: {e}")
        
        end_time = time.time()
        latency = end_time - start_time
        
        results.append({
            "run_id": run_label,
            "timestamp": datetime.now().isoformat(),
            "question_id": q_id,
            "question": question,
            "provider": provider,
            "model": model,
            "response": content,
            "latency_seconds": latency,
            "error": error,
            "variant": variant
        })
        print(f"Done ({latency:.2f}s)")

    # 5. Save Results
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"eval_{variant}_{provider}_{timestamp}.parquet"
    output_path = RESULTS_DIR / filename
    
    results_df = pd.DataFrame(results)
    
    # Needs pyarrow or fastparquet. 'uv run' should handle it if installed.
    # Check if we need to install 'fastparquet' or 'pyarrow'. 
    # Usually pandas needs one for parquet. We'll default to csv if parquet fails, or assume environment is good.
    # Let's write both for safety now.
    
    try:
        results_df.to_parquet(output_path)
        print(f"Saved parquet results to {output_path}")
    except ImportError:
        csv_path = str(output_path).replace(".parquet", ".csv")
        results_df.to_csv(csv_path, index=False)
        print(f"Saved CSV results (parquet missing) to {csv_path}")
        
    # Also save a readable CSV for quick check
    readable_csv = RESULTS_DIR / f"eval_V0_{provider}_{timestamp}_readable.csv"
    results_df.to_csv(readable_csv, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Evaluation (V0 or V1)")
    parser.add_argument("--provider", type=str, default=settings.default_provider, help="Provider name")
    parser.add_argument("--model", type=str, default=None, help="Model name (defaults to env settings)")
    parser.add_argument("--variant", type=str, default="V0", choices=["V0", "V1"], help="Evaluation variant")
    
    args = parser.parse_args()
    
    # Determine model default if not provided
    if not args.model:
        if args.provider == "gemini":
            args.model = settings.default_model_google
        elif args.provider == "openrouter":
            args.model = settings.default_model_openrouter
            
    asyncio.run(run_evaluation(args.provider, args.model, args.variant))
