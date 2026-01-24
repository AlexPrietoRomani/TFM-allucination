import pandas as pd
from pathlib import Path
from glob import glob

RESULTS_DIR = Path("eval/results/V0")

def load_latest_results(variant):
    files = sorted(glob(str(RESULTS_DIR / f"eval_{variant}_*.csv"))) # Using csv as they are readable/safe
    if not files:
        # Try parquet
        files = sorted(glob(str(RESULTS_DIR / f"eval_{variant}_*.parquet")))
    
    if not files:
        print(f"No results found for {variant}")
        return None
        
    latest = files[-1]
    print(f"Loading latest {variant}: {latest}")
    try:
        return pd.read_parquet(latest)
    except:
        return pd.read_csv(latest)

def generate_comparison():
    v0 = load_latest_results("V0")
    v1 = load_latest_results("V1")
    
    if v0 is None or v1 is None:
        print("Could not load both variants.")
        return

    # Merge
    merged = pd.merge(
        v0[["question_id", "question", "response", "latency_seconds"]],
        v1[["question_id", "response", "latency_seconds"]],
        on="question_id",
        suffixes=("_v0", "_v1")
    )
    
    report = "# Reporte Comparativo V0 (Baseline) vs V1 (RAG)\n\n"
    report += f"**Total Preguntas**: {len(merged)}\n\n"
    
    # Latency Stats
    avg_lat_v0 = merged['latency_seconds_v0'].mean()
    avg_lat_v1 = merged['latency_seconds_v1'].mean()
    report += "## Latencia Promedio\n"
    report += f"- V0: {avg_lat_v0:.2f}s\n"
    report += f"- V1: {avg_lat_v1:.2f}s\n"
    report += f"- Impacto RAG: +{avg_lat_v1 - avg_lat_v0:.2f}s\n\n"
    
    # Heuristic Quality Check (Citation Presence)
    # We check if V1 response contains brackets like "[Source:" or "ID:"
    merged["v1_has_citation"] = merged["response_v1"].apply(lambda x: "[Source:" in str(x) or "ID:" in str(x))
    citation_rate = merged["v1_has_citation"].mean() * 100
    
    report += "## Calidad Heurística\n"
    report += f"- Tasa de Citación en V1: {citation_rate:.1f}%\n\n"
    
    report += "## Detalle por Pregunta\n\n"
    for idx, row in merged.iterrows():
        report += f"### Q{row['question_id']}: {row['question']}\n\n"
        
        report += "**V0 (Baseline)**\n"
        report += f"> {str(row['response_v0'])[:300]}...\n\n"
        
        report += "**V1 (RAG)**\n"
        # Escape markdown chars if needed, but simple block quote is usually fine
        report += f"> {str(row['response_v1'])[:500]}...\n\n"
        
        report += f"*Cita detectada: {'✅' if row['v1_has_citation'] else '❌'}*\n"
        report += "---\n\n"
        
    output_path = Path("reports/v0_vs_v1.md")
    output_path.parent.mkdir(exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)
        
    print(f"Report generated at {output_path}")

if __name__ == "__main__":
    generate_comparison()
