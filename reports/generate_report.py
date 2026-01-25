import pandas as pd
from pathlib import Path
from glob import glob

RESULTS_DIR = Path("eval/results/Comparison")

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
            return pd.read_csv(latest)
    except Exception as e:
        print(f"Error cargando archivo: {e}")
        return None

def generate_report():
    df = load_latest_comparison()
    
    if df is None:
        return

    # Asegurar que existan columnas (compatibilidad hacia atrás)
    required_cols = ["response_v0", "response_v1", "latency_v0", "latency_v1", "question", "question_id"]
    for col in required_cols:
        if col not in df.columns:
            print(f"Falta la columna '{col}' en los resultados.")
            return

    report = "# Reporte Comparativo V0 (Baseline) vs V1 (RAG)\n\n"
    report += f"**Fecha Ejecución**: {df['timestamp'].iloc[0] if 'timestamp' in df else 'N/A'}\n"
    report += f"**Modelo**: {df['model'].iloc[0] if 'model' in df else 'Desconocido'}\n"
    report += f"**Total Preguntas**: {len(df)}\n\n"
    
    # --- Métricas ---
    avg_lat_v0 = df['latency_v0'].mean()
    avg_lat_v1 = df['latency_v1'].mean()
    
    # Heurística: Verificar si hay Citación en V1
    # Buscar [Fuente: o ID: o marcadores típicos de citación
    def has_citation(text):
        t = str(text)
        return "[Source:" in t or "ID:" in t or "Source:" in t or "[Fuente:" in t
        
    df["v1_cited"] = df["response_v1"].apply(has_citation)
    citation_rate = df["v1_cited"].mean() * 100
    
    report += "## 1. Métricas de Desempeño\n\n"
    report += "| Métrica | V0 (Baseline) | V1 (RAG) | Delta |\n"
    report += "|---|---|---|---|\n"
    report += f"| **Latencia Promedio** | {avg_lat_v0:.2f}s | {avg_lat_v1:.2f}s | {avg_lat_v1 - avg_lat_v0:+.2f}s |\n"
    report += f"| **Tasa de Citación** | N/A | {citation_rate:.1f}% | - |\n\n"

    report += "## 2. Detalle de Respuestas\n\n"
    
    for idx, row in df.iterrows():
        q_id = row['question_id']
        question = row['question']
        
        report += f"### Q{q_id}: {question}\n\n"
        
        # V0
        v0_text = str(row['response_v0']).replace("\n", "\n> ")
        if not v0_text or v0_text == "nan":
            v0_text = f"*(Error or Empty)*: {row.get('error_v0', 'N/A')}"
            
        report += f"**🤖 V0 (Baseline)** ({row['latency_v0']:.2f}s)\n"
        report += f"> {v0_text}\n\n"
        
        # V1
        v1_text = str(row['response_v1']).replace("\n", "\n> ")
        if not v1_text or v1_text == "nan":
            v1_text = f"*(Error or Empty)*: {row.get('error_v1', 'N/A')}"
            
        cited_icon = "✅" if row['v1_cited'] else "❌"
        
        report += f"**📚 V1 (RAG)** ({row['latency_v1']:.2f}s) {cited_icon}\n"
        report += f"> {v1_text}\n\n"
        
        report += "---\n\n"

    output_path = Path("reports/v0_vs_v1_comparative.md")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
        
    print(f"Reporte generado exitosamente: {output_path}")

if __name__ == "__main__":
    generate_report()
