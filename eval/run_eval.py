"""
run_eval.py — Evaluador de RAG v1 (Comparativa)

Carga un banco de preguntas (`question_bank_v1.csv`) y las envía al motor 
RAG clásico para generar respuestas e indexar tiempos de respuesta, 
guardando la comparativa en bruto en `eval/results/Comparison`.

Uso:
    uv run python eval/run_eval.py [OPCIONES]

Opciones:
    --limit N        Procesar un número máximo fijo de N preguntas del banco.
"""

import argparse
import asyncio
import pandas as pd
import time
import os
from pathlib import Path
from datetime import datetime
from src.core.providers.factory import ProviderFactory
from pathlib import Path
import sys

# Asegurar que el directorio raíz esté en el PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.core.config.settings import settings
from src.chat.rag import RAGEngine

# Configuration
INPUT_FILE = Path("eval/question_bank_v1.csv")
RESULTS_DIR = Path("eval/results/Comparison")

def load_questions():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Question bank not found at {INPUT_FILE}")
    # Ensure ID is treated as string to avoid type mismatches
    df = pd.read_csv(INPUT_FILE, dtype={'id': str})
    return df

async def run_comparative_evaluation(provider: str, model: str, run_label: str = "default", limit: int = 0):
    print(f"Starting COMPARATIVE evaluation (V0 vs V1) with {provider}/{model}...")
    
    # 1. Load Data
    df = load_questions()
    if limit > 0:
        print(f"Limiting to first {limit} questions.")
        df = df.head(limit)
        
    print(f"Loaded {len(df)} questions.")
    
    # 2. Initialize Engines
    print("Initializing LLM and RAG Engine...")
    try:
        # Shared LLM - Bypass Factory redirect if we really want local Ollama testing for Evals.
        if provider == "ollama":
            from langchain_community.llms import Ollama
            llm = Ollama(model=model, base_url=settings.ollama_base_url)
        else:
            llm = ProviderFactory.get_provider(provider, model)
            
        # RAG Engine (V1)
        rag_engine = RAGEngine()
        rag_chain = rag_engine.get_chain(llm)
        
    except Exception as e:
        print(f"Failed to initialize engines: {e}")
        return

    # 3. Iterate & Evaluate
    results = []
    
    for index, row in df.iterrows():
        print(f"[{index+1}/{len(df)}] Processing Q{row['id']}...", end=" ", flush=True)
        
        res = evaluate_row_v0_v1(row, llm, rag_chain, provider, model, run_label)
        results.append(res)
        
        # Rate limiting pause (Aggressive for free tier)
        time.sleep(15)
        print(f"Done (V0: {res['latency_v0']:.2f}s | V1: {res['latency_v1']:.2f}s)")

    # 4. Save Combined Results
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_base = f"eval_comparison_{provider}_{timestamp}"
    
    results_df = pd.DataFrame(results)
    
    # Save Parquet
    parquet_path = RESULTS_DIR / f"{filename_base}.parquet"
    try:
        results_df.to_parquet(parquet_path)
        print(f"Saved parquet results to {parquet_path}")
    except ImportError:
        print("Parquet support missing, skipping parquet save.")
        
    # Save CSV (always useful for quick debug)
    csv_path = RESULTS_DIR / f"{filename_base}.csv"
    results_df.to_csv(csv_path, index=False)
    print(f"Saved CSV results to {csv_path}")

def evaluate_row_v0_v1(row, llm, rag_chain, provider, model, run_label="default"):
    q_id = str(row['id'])
    question = row['question']
    
    # --- V0 Execution (Baseline) ---
    start_v0 = time.time()
    try:
        raw_resp = llm.invoke(question)
        if hasattr(raw_resp, 'content'):
            resp_v0 = raw_resp.content
        else:
            resp_v0 = str(raw_resp)
        error_v0 = None
    except Exception as e:
        resp_v0 = ""
        error_v0 = str(e)
        print(f"  [ERROR V0]: {e}")
    time_v0 = time.time() - start_v0
    
    # --- V1 Execution (RAG) ---
    start_v1 = time.time()
    try:
        # RAG returns a string directly from the chain defined in rag.py
        resp_v1 = rag_chain.invoke(question)
        error_v1 = None
    except Exception as e:
        resp_v1 = ""
        error_v1 = str(e)
        print(f"  [ERROR V1]: {e}")
    time_v1 = time.time() - start_v1
    
    return {
        "run_id": run_label,
        "timestamp": datetime.now().isoformat(),
        "question_id": q_id,
        "question": question,
        "provider": provider,
        "model": model,
        "response_v0": resp_v0,
        "latency_v0": time_v0,
        "error_v0": error_v0,
        "response_v1": resp_v1,
        "latency_v1": time_v1,
        "error_v1": error_v1
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar Evaluación Comparativa (V0 vs V1)")
    parser.add_argument("--provider", type=str, default=settings.default_provider, help="Nombre del proveedor")
    parser.add_argument("--model", type=str, default=None, help="Nombre del modelo")
    parser.add_argument("--limit", type=int, default=0, help="Limitar número de preguntas (0 para todas)")
    parser.add_argument("--clean", action="store_true", help="Limpiar resultados anteriores antes de ejecutar")
    
    args = parser.parse_args()
    
    # Valores por defecto
    if not args.model:
        if args.provider == "gemini":
            args.model = settings.default_model_google
        elif args.provider == "openrouter":
            args.model = settings.default_model_openrouter
        # Para ollama, el usuario suele especificarlo, o usamos default
        elif args.provider == "ollama":
            args.model = "gpt-oss:20b" 
            
    # Lógica de limpieza
    if args.clean:
        import shutil
        if RESULTS_DIR.exists():
            print(f"Limpiando directorio de resultados: {RESULTS_DIR}")
            shutil.rmtree(RESULTS_DIR)
            
    try:
        asyncio.run(run_comparative_evaluation(args.provider, args.model, limit=args.limit))
    finally:
        # Limpieza para Ollama para liberar RAM
        if args.provider == "ollama" and args.model:
            from src.core.providers.ollama import OllamaProvider
            OllamaProvider.unload_model(args.model)
