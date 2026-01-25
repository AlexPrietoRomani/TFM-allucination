import pandas as pd
from pathlib import Path
from glob import glob
import json
import argparse
import sys

# Paths
RESULTS_DIR = Path("eval/results")
COMPARISON_DIR = RESULTS_DIR / "Comparison"
METRICS_DIR = RESULTS_DIR / "Metrics"
V2_DIR = RESULTS_DIR / "V2"
V0_DIR = RESULTS_DIR / "V0"

def load_v0_results():
    # V0 usually in Comparison files or standalone if we had them. 
    # Current flow puts V0 in comparison. Let's try to extract from comparison if available.
    return load_comparison_results()

def load_comparison_results():
    files = sorted(glob(str(COMPARISON_DIR / "eval_comparison_*.parquet")))
    if not files:
        files = sorted(glob(str(COMPARISON_DIR / "eval_comparison_*.csv")))
    
    if not files:
        return pd.DataFrame()
        
    latest = files[-1]
    print(f"   -> Cargando datos comparativos (V0/V1): {latest}")
    try:
        if latest.endswith(".parquet"):
            df = pd.read_parquet(latest)
        else:
            df = pd.read_csv(latest, dtype={'question_id': str})
        
        if 'question_id' not in df.columns and 'id' in df.columns:
            df = df.rename(columns={'id': 'question_id'})
            
        df['question_id'] = df['question_id'].astype(str)
        return df
    except Exception as e:
        print(f"Error loading comparison: {e}")
        return pd.DataFrame()

def load_v2_results():
    files = sorted(glob(str(V2_DIR / "eval_v2_*.json")))
    if not files:
        return pd.DataFrame()
        
    latest = files[-1]
    print(f"   -> Cargando datos V2 (Agente): {latest}")
    try:
        with open(latest, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        df_v2 = pd.DataFrame(data)
        if 'question_id' in df_v2.columns:
            df_v2['question_id'] = df_v2['question_id'].astype(str)
            
        # Standardize cols
        rename_map = {
            "response": "response_v2",
            "latency": "latency_v2",
            "faithfulness_score": "faith_v2",
            "retries": "retries_v2"
        }
        df_v2 = df_v2.rename(columns={k:v for k,v in rename_map.items() if k in df_v2.columns})
        
        # Select relevant cols
        cols = ['question_id', 'response_v2', 'latency_v2', 'faith_v2', 'retries_v2']
        return df_v2[[c for c in cols if c in df_v2.columns]]
    except Exception as e:
        print(f"Error loading V2: {e}")
        return pd.DataFrame()

def load_metrics():
    """Carga métricas detalladas V1 (FactScore, etc)."""
    merged = pd.DataFrame()
    
    # 1. Faith/Rel
    faith_files = sorted(glob(str(METRICS_DIR / "metrics_eval_*.csv")))
    if faith_files:
        df = pd.read_csv(faith_files[-1], dtype={'question_id': str})
        if 'question_id' in df.columns:
             merged = df[['question_id', 'faithfulness_score', 'relevance_score']]

    # 2. FactScore
    fs_files = sorted(glob(str(METRICS_DIR / "factscore_eval*.csv")))
    if fs_files:
        df = pd.read_csv(fs_files[-1], dtype={'question_id': str})
        if not merged.empty:
            merged = pd.merge(merged, df, on='question_id', how='outer')
        else:
            merged = df
            
    if not merged.empty:
         print(f"   -> Cargando métricas detalladas V1 (FactScore/Faith/Rel)")
         
    return merged

def generate_report(mode="all"):
    print(f"Generando reporte. Modo: {mode.upper()}")
    
    # Base: Comparison (contains V0 and usually V1 base)
    df_main = load_comparison_results()
    
    # Dataframes placeholders
    df_v2 = pd.DataFrame()
    df_metrics = pd.DataFrame()
    
    # Load requested data
    if mode in ["v1", "all"]:
        df_metrics = load_metrics()
    if mode in ["v2", "all"]:
        df_v2 = load_v2_results()
        
    # Validation
    if df_main.empty and df_v2.empty:
        print("❌ No se encontraron datos para generar el reporte.")
        return

    # Merge Logic
    # Start with whatever we have. If we have main, start there.
    final_df = df_main.copy() if not df_main.empty else df_v2.copy()
    
    if not df_main.empty:
        if not df_metrics.empty:
            final_df = pd.merge(final_df, df_metrics, on='question_id', how='left')
        if not df_v2.empty:
             final_df = pd.merge(final_df, df_v2, on='question_id', how='left')
    
    # Ensure correct sorting or ID management
    if 'question_id' in final_df.columns:
        # Try numeric sort
        try:
             final_df['sort_id'] = final_df['question_id'].astype(int)
             final_df = final_df.sort_values('sort_id').drop('sort_id', axis=1)
        except:
             pass

    # --- REPORT GENERATION ---
    timestamp = pd.Timestamp.now().strftime("%Y%m%d_%H%M%S")
    report_title = f"Reporte Evaluación TFM - {mode.upper()}"
    filename = f"reports/reporte_tfm_{mode}_{timestamp}.md"
    
    md = f"# {report_title}\n\n"
    md += f"**Fecha**: {pd.Timestamp.now()}\n"
    md += f"**Total Casos**: {len(final_df)}\n\n"
    
    # 1. Summary Table
    md += "## 1. Resumen de Métricas\n\n"
    md += "| Métrica | V0 (Baseline) | V1 (RAG) | V2 (Agente) |\n"
    md += "|---|---|---|---|\n"
    
    # Calculate avgs
    # V0
    lat_v0 = final_df['latency_v0'].mean() if 'latency_v0' in final_df else 0
    
    # V1
    lat_v1 = final_df['latency_v1'].mean() if 'latency_v1' in final_df else 0
    faith_v1 = final_df['faithfulness_score'].mean() if 'faithfulness_score' in final_df else 0
    fs_v1 = final_df['factscore'].mean() if 'factscore' in final_df else 0
    
    # V2
    lat_v2 = final_df['latency_v2'].mean() if 'latency_v2' in final_df else 0
    faith_v2 = final_df['faith_v2'].mean() if 'faith_v2' in final_df else 0
    
    md += f"| Latencia Promedio (s) | {lat_v0:.2f} | {lat_v1:.2f} | {lat_v2:.2f} |\n"
    md += f"| Fidelidad (0-1) | N/A | {faith_v1:.2f} | {faith_v2:.2f} |\n"
    md += f"| FactScore | N/A | {fs_v1:.2f} | (Interno) |\n\n"
    
    # 2. Detail
    md += "## 2. Detalle por Pregunta\n\n"
    for _, row in final_df.iterrows():
        qid = row.get('question_id', 'N/A')
        q = row.get('question', 'N/A')
        
        md += f"### Q{qid}: {q}\n\n"
        
        if mode in ["v0", "all"] and 'response_v0' in row:
             md += f"**V0 (Baseline)** ({row.get('latency_v0',0):.1f}s)\n"
             md += f"> {str(row.get('response_v0', '')).replace(chr(10), chr(10)+'> ')}\n\n"

        if mode in ["v1", "all"] and 'response_v1' in row:
             md += f"**V1 (RAG)** [Fidelidad: {row.get('faithfulness_score', 'N/A')}] ({row.get('latency_v1',0):.1f}s)\n"
             md += f"> {str(row.get('response_v1', '')).replace(chr(10), chr(10)+'> ')}\n\n"

        if mode in ["v2", "all"] and 'response_v2' in row:
             md += f"**V2 (Agente)** [Fidelidad: {row.get('faith_v2', 'N/A')} | Retries: {row.get('retries_v2',0)}] ({row.get('latency_v2',0):.1f}s)\n"
             md += f"> {str(row.get('response_v2', '')).replace(chr(10), chr(10)+'> ')}\n\n"
        
        md += "---\n"

    # Save
    out_path = Path(filename)
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"✅ Reporte guardado en: {out_path}")
    return str(out_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="all", choices=["all", "v0", "v1", "v2"], help="Versiones a incluir en el reporte")
    args = parser.parse_args()
    
    generate_report(args.mode)
