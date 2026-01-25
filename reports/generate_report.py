import pandas as pd
from pathlib import Path
from glob import glob
import json

RESULTS_DIR = Path("eval/results/Comparison")
METRICS_DIR = Path("eval/results/Metrics")

def load_latest_comparison():
    # Buscar el último parquet o csv en la carpeta de comparación
    files = sorted(glob(str(RESULTS_DIR / "eval_comparison_*.parquet")))
    if not files:
        files = sorted(glob(str(RESULTS_DIR / "eval_comparison_*.csv")))
    
    if not files:
        print("No se encontraron resultados comparativos.")
        return None
        
    latest = files[-1]
    print(f"Cargando última comparación: {latest}")
    try:
        if latest.endswith(".parquet"):
            return pd.read_parquet(latest)
        else:
            return pd.read_csv(latest, dtype={'question_id': str})
    except Exception as e:
        print(f"Error cargando archivo: {e}")
        return None

def load_metrics():
    """Carga y combina métricas de Faithfulness/Relevance y FactScore."""
    merged_metrics = pd.DataFrame()
    
    # 1. Faithfulness/Relevance
    faith_files = sorted(glob(str(METRICS_DIR / "metrics_eval_*.csv")))
    if faith_files:
        latest_faith = faith_files[-1]
        print(f"Cargando métricas de fidelidad: {latest_faith}")
        df_faith = pd.read_csv(latest_faith, dtype={'question_id': str})
        # Mantener solo columnas clave
        cols = ['question_id', 'faithfulness_score', 'relevance_score', 'faithfulness_reason', 'relevance_reason']
        # Intersección de columnas existentes
        cols = [c for c in cols if c in df_faith.columns]
        df_faith = df_faith[cols]
        merged_metrics = df_faith
        
    # 2. FactScore
    fs_files = sorted(glob(str(METRICS_DIR / "factscore_eval*.csv")))
    if fs_files:
        latest_fs = fs_files[-1]
        print(f"Cargando métricas FactScore: {latest_fs}")
        df_fs = pd.read_csv(latest_fs, dtype={'question_id': str})
        cols = ['question_id', 'factscore', 'supported', 'total_claims', 'breakdown_json']
        cols = [c for c in cols if c in df_fs.columns]
        df_fs = df_fs[cols]
        
        if not merged_metrics.empty:
            merged_metrics = pd.merge(merged_metrics, df_fs, on='question_id', how='outer')
        else:
            merged_metrics = df_fs
            
    return merged_metrics

def generate_report():
    df = load_latest_comparison()
    
    if df is None:
        return

    # Asegurar tipo str en IDs
    if 'question_id' in df.columns:
        df['question_id'] = df['question_id'].astype(str)

    # Cargar y unir métricas adicionales
    df_metrics = load_metrics()
    if not df_metrics.empty:
        df = pd.merge(df, df_metrics, on='question_id', how='left')

    report = "# Reporte Final Integrado: Chatbot Arándanos (V0 vs V1)\n\n"
    report += f"**Fecha Ejecución**: {df['timestamp'].iloc[0] if 'timestamp' in df else 'N/A'}\n"
    report += f"**Modelo Evaluado**: {df['model'].iloc[0] if 'model' in df else 'gpt-oss:20b (Ollama)'}\n"
    report += f"**Total Preguntas Evaluadas**: {len(df)}\n\n"
    
    # --- Métricas Globales ---
    avg_lat_v0 = df['latency_v0'].mean() if 'latency_v0' in df else 0
    avg_lat_v1 = df['latency_v1'].mean() if 'latency_v1' in df else 0
    
    # Heurística: Citación
    def has_citation(text):
        t = str(text)
        return "[Source:" in t or "ID:" in t or "Source:" in t or "[Fuente:" in t or "Fuente:" in t
        
    df["v1_cited"] = df["response_v1"].apply(has_citation)
    citation_rate = df["v1_cited"].mean() * 100
    
    # Promedios de Métricas Avanzadas (si existen)
    avg_faith = df['faithfulness_score'].mean() if 'faithfulness_score' in df else None
    avg_rel = df['relevance_score'].mean() if 'relevance_score' in df else None
    avg_fs = df['factscore'].mean() if 'factscore' in df else None
    
    report += "## 1. Resumen de Desempeño\n\n"
    report += "| Métrica | V0 (Baseline) | V1 (RAG) | Delta/Score |\n"
    report += "|---|---|---|---|\n"
    report += f"| **Latencia** | {avg_lat_v0:.2f}s | {avg_lat_v1:.2f}s | {avg_lat_v1 - avg_lat_v0:+.2f}s |\n"
    report += f"| **Tasa de Citación** | N/A | {citation_rate:.1f}% | - |\n"
    
    if avg_faith is not None:
        report += f"| **Fidelidad (Faithfulness)** | - | {avg_faith:.2f} | 0.0 - 1.0 |\n"
    if avg_rel is not None:
        report += f"| **Relevancia Contextual** | - | {avg_rel:.2f} | 0.0 - 1.0 |\n"
    if avg_fs is not None:
        report += f"| **FactScore (Hechos)** | - | {avg_fs:.2f} | 0.0 - 1.0 |\n"

    report += "\n\n## 2. Detalle de Respuestas y Evaluación\n\n"
    
    for idx, row in df.iterrows():
        q_id = row.get('question_id', 'N/A')
        question = row.get('question', 'N/A')
        
        report += f"### Q{q_id}: {question}\n\n"
        
        # V1 Response
        v1_text = str(row.get('response_v1', '')).replace("\n", "\n> ")
        cited_icon = "✅" if row.get('v1_cited') else "⚠️"
        
        report += f"**📚 V1 (RAG) Generado** {cited_icon}\n"
        report += f"> {v1_text}\n\n"
        
        # Metrics Detail
        report += f"**Evaluación de Calidad:**\n"
        if pd.notna(row.get('faithfulness_score')):
            report += f"- **Fidelidad**: {row['faithfulness_score']:.2f} _({row.get('faithfulness_reason', '')})_\n"
        if pd.notna(row.get('relevance_score')):
            report += f"- **Relevancia**: {row['relevance_score']:.2f} _({row.get('relevance_reason', '')})_\n"
        if pd.notna(row.get('factscore')):
            fs_info = f"{row['factscore']:.2f} ({row.get('supported',0)}/{row.get('total_claims',0)} claims)"
            report += f"- **FactScore**: {fs_info}\n"
            
            # Desglose FactScore
            if pd.notna(row.get('breakdown_json')):
                try:
                    bk = str(row['breakdown_json']).replace("'", '"') # Basic fix for stringified list
                    # It might be safely parsed if valid json, but pandas stringifies python objects often with single quotes
                    # Let's try to just print it cleanly if parsing fails
                    report += "  - *Desglose de Hechos:*\n"
                    # Simple heuristic formatting
                    items = str(row['breakdown_json'])
                    report += f"    - `{items}`\n"
                except:
                    pass

        report += "\n---\n\n"

    output_path = Path("reports/final_integrated_report.md")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
        
    print(f"Reporte Final generado exitosamente: {output_path}")

if __name__ == "__main__":
    generate_report()
