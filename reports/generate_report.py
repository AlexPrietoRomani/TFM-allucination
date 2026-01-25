import pandas as pd
from pathlib import Path
from glob import glob
import json

RESULTS_DIR = Path("eval/results/Comparison")
METRICS_DIR = Path("eval/results/Metrics")
V2_DIR = Path("eval/results/V2")

def load_latest_comparison():
    # Buscar el último parquet o csv en la carpeta de comparación
    files = sorted(glob(str(RESULTS_DIR / "eval_comparison_*.parquet")))
    if not files:
        files = sorted(glob(str(RESULTS_DIR / "eval_comparison_*.csv")))
    
    if not files:
        print("No se encontraron resultados comparativos V0/V1.")
        return None
        
    latest = files[-1]
    print(f"Cargando última comparación V0/V1: {latest}")
    try:
        if latest.endswith(".parquet"):
            return pd.read_parquet(latest)
        else:
            return pd.read_csv(latest, dtype={'question_id': str})
    except Exception as e:
        print(f"Error cargando archivo: {e}")
        return None

def load_v2_results():
    files = sorted(glob(str(V2_DIR / "eval_v2_*.json")))
    if not files:
        print("No se encontraron resultados de V2.")
        return pd.DataFrame()
        
    latest = files[-1]
    print(f"Cargando últimos resultados V2: {latest}")
    try:
        with open(latest, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert to DF
        df_v2 = pd.DataFrame(data)
        if 'question_id' in df_v2.columns:
            df_v2['question_id'] = df_v2['question_id'].astype(str)
            
        # Rename cols to avoid conflict
        df_v2 = df_v2.rename(columns={
            "response": "response_v2",
            "latency": "latency_v2",
            "faithfulness_score": "faith_v2",
            "retries": "retries_v2"
        })
        return df_v2[['question_id', 'response_v2', 'latency_v2', 'faith_v2', 'retries_v2']]
    except Exception as e:
        print(f"Error cargando V2: {e}")
        return pd.DataFrame()

def load_metrics():
    """Carga y combina métricas de Faithfulness/Relevance y FactScore para V1."""
    merged_metrics = pd.DataFrame()
    
    # 1. Faithfulness/Relevance (V1 metrics usually)
    faith_files = sorted(glob(str(METRICS_DIR / "metrics_eval_*.csv")))
    if faith_files:
        latest_faith = faith_files[-1]
        df_faith = pd.read_csv(latest_faith, dtype={'question_id': str})
        cols = ['question_id', 'faithfulness_score', 'relevance_score']
        cols = [c for c in cols if c in df_faith.columns]
        df_faith = df_faith[cols]
        merged_metrics = df_faith
        
    # 2. FactScore (V1 mostly)
    fs_files = sorted(glob(str(METRICS_DIR / "factscore_eval*.csv")))
    if fs_files:
        latest_fs = fs_files[-1]
        df_fs = pd.read_csv(latest_fs, dtype={'question_id': str})
        cols = ['question_id', 'factscore', 'supported', 'total_claims']
        cols = [c for c in cols if c in df_fs.columns]
        df_fs = df_fs[cols]
        
        if not merged_metrics.empty:
            merged_metrics = pd.merge(merged_metrics, df_fs, on='question_id', how='outer')
        else:
            merged_metrics = df_fs
            
    return merged_metrics

def generate_report():
    df = load_latest_comparison()
    if df is None: return

    if 'question_id' in df.columns:
        df['question_id'] = df['question_id'].astype(str)

    # Merge Metrics V1
    df_metrics = load_metrics()
    if not df_metrics.empty:
        df = pd.merge(df, df_metrics, on='question_id', how='left')
        
    # Merge V2
    df_v2 = load_v2_results()
    if not df_v2.empty:
        df = pd.merge(df, df_v2, on='question_id', how='left')

    report = "# Reporte Final Integrado: Chatbot Arándanos (V0 vs V1 vs V2)\n\n"
    report += f"**Fecha Ejecución**: {pd.Timestamp.now()}\n"
    report += f"**Total Preguntas**: {len(df)}\n\n"
    
    # --- Métricas Globales ---
    avg_lat_v0 = df['latency_v0'].mean() if 'latency_v0' in df else 0
    avg_lat_v1 = df['latency_v1'].mean() if 'latency_v1' in df else 0
    avg_lat_v2 = df['latency_v2'].mean() if 'latency_v2' in df else 0
    
    avg_faith_v1 = df['faithfulness_score'].mean() if 'faithfulness_score' in df else 0
    avg_faith_v2 = df['faith_v2'].mean() if 'faith_v2' in df else 0
    
    avg_fact_v1 = df['factscore'].mean() if 'factscore' in df else 0
    
    report += "## 1. Resumen Comparativo de Desempeño\n\n"
    report += "| Métrica | V0 (Baseline) | V1 (RAG) | V2 (Agente) |\n"
    report += "|---|---|---|---|\n"
    report += f"| **Latencia (s)** | {avg_lat_v0:.2f} | {avg_lat_v1:.2f} | {avg_lat_v2:.2f} |\n"
    report += f"| **Fidelidad (0-1)** | N/A | {avg_faith_v1:.2f} | {avg_faith_v2:.2f} |\n"
    report += f"| **FactScore** | N/A | {avg_fact_v1:.2f} | N/A (Internal) |\n"

    report += "\n\n## 2. Detalle por Pregunta\n\n"
    
    for idx, row in df.iterrows():
        q_id = row.get('question_id', 'N/A')
        question = row.get('question', 'N/A')
        
        report += f"### Q{q_id}: {question}\n\n"
        
        # Responses
        v1_text = str(row.get('response_v1', 'N/A')).replace("\n", "\n>")
        v2_text = str(row.get('response_v2', 'N/A')).replace("\n", "\n>")
        
        report += f"**V1 (RAG)** [Fidelidad: {row.get('faithfulness_score', 'N/A'):.2f}]\n"
        report += f"> {v1_text}\n\n"
        
        report += f"**V2 (Agente)** [Fidelidad: {row.get('faith_v2', 'N/A'):.2f} | Retries: {row.get('retries_v2', 0)}]\n"
        report += f"> {v2_text}\n\n"
        
        report += "---\n\n"

    output_path = Path("reports/final_integrated_report.md")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
        
    print(f"Reporte Final generado exitosamente: {output_path}")

if __name__ == "__main__":
    generate_report()
