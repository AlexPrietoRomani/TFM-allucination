import pandas as pd
import json
import os
from scipy.stats import kruskal, mannwhitneyu

def load_data(file_path):
    """Carga los resultados de un archivo JSONL manejando errores."""
    data = []
    bad_lines = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                data.append(json.loads(line))
            except Exception:
                bad_lines += 1
    if bad_lines > 0:
        print(f"⚠️  Advertencia: Se omitieron {bad_lines} líneas corruptas en {file_path}")
    return pd.DataFrame(data)

def analyze_factor(df, factor_name, metric_name):
    """Realiza Kruskal-Wallis y Mann-Whitney U para un factor individual."""
    groups = []
    labels = []
    
    for val in df[factor_name].unique():
        series = df[df[factor_name] == val][metric_name].dropna()
        if len(series) >= 2:  # Se necesitan al menos 2 puntos por grupo
            groups.append(series)
            labels.append(val)
            
    if len(groups) < 2:
        return None, f"No hay suficientes grupos ({len(groups)}) para {factor_name}"

    try:
        stat, p_val = kruskal(*groups)
    except ValueError as e:
        return None, f"Error en Kruskal-Wallis: {str(e)}"
        
    # Calcular medias y medianas para ranking
    summary = []
    for group, label in zip(groups, labels):
        summary.append({
            'Factor': label,
            'Count': len(group),
            'Mean': group.mean(),
            'Median': group.median()
        })
        
    summary_df = pd.DataFrame(summary).sort_values(by='Mean', ascending=False)
    
    # Post-hoc: Comparar el "Mejor" (Top 1 por media) contra los demás usando Mann-Whitney U
    posthoc = []
    if len(summary_df) > 1:
        best_factor = summary_df.iloc[0]['Factor']
        best_data = df[df[factor_name] == best_factor][metric_name].dropna()
        
        for i in range(1, len(summary_df)):
            other_factor = summary_df.iloc[i]['Factor']
            other_data = df[df[factor_name] == other_factor][metric_name].dropna()
            
            try:
                stat_u, p_u = mannwhitneyu(best_data, other_data, alternative='two-sided')
                # Si p_u >= 0.05, estadísticamente es igual al mejor.
                posthoc.append({
                    'Other': other_factor,
                    'p-value': p_u,
                    'Stat. Equal': 'Sí' if p_u >= 0.05 else 'No'
                })
            except Exception:
                pass
                
    return {
        'factor': factor_name,
        'metric': metric_name,
        'overall_p': p_val,
        'summary': summary_df,
        'posthoc': pd.DataFrame(posthoc) if posthoc else pd.DataFrame()
    }, None

def main():
    file_path = 'eval/results/Matrix/eval_results_matrix.jsonl'
    output_dir = 'eval/results/Matrix'
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(file_path):
        print(f"❌ Error: No se encontró el archivo '{file_path}'")
        return
        
    print(f"📂 Cargando datos desde {file_path}...")
    df = load_data(file_path)
    
    if df.empty:
        print("❌ Error: El dataframe cargado está vacío.")
        return
        
    # Filtrar por los generadores solicitados
    target_generators = ["deepseek-r1:8b", "qwen2.5:3b", "gpt-oss:20b"]
    print(f"🔍 Filtrando para los modelos: {', '.join(target_generators)}")
    df_filtered = df[df['generator'].isin(target_generators)].copy()
    
    if df_filtered.empty:
        print("⚠️ Advertencia: No hay registros que coincidan con los generadores solicitados.")
        return
        
    # Identificar métricas terminadas en '_score'
    metrics = [col for col in df_filtered.columns if col.endswith('_score')]
    factors = ['architecture', 'embedding', 'chunk_strategy', 'db_motor', 'generator']
    
    # Asegurar que las métricas sean numéricas
    for m in metrics:
        df_filtered[m] = pd.to_numeric(df_filtered[m], errors='coerce')
        
    print(f"📊 Métricas encontradas ({len(metrics)}): {', '.join(metrics)}")
    
    # Crear columna de Combinación
    df_filtered['Combination'] = df_filtered.apply(
        lambda x: f"{x['architecture']} | {x['embedding']} | {x['chunk_strategy']} | {x['db_motor']} | {x['generator']}", axis=1
    )
    
    report = []
    report.append("# 📈 Informe de Análisis Estadístico del RAG")
    report.append(f"Modelos evaluados: {', '.join(target_generators)}")
    report.append(f"Total registros analizados: {len(df_filtered)}")
    report.append("\n---")
    
    for metric in metrics:
        report.append(f"\n## 🎯 Métrica: `{metric.upper().replace('_SCORE', '')}`")
        
        # --- 1. Análisis de Factores Individuales ---
        report.append("\n### 🔍 Análisis por Factor Individual")
        for factor in factors:
            res, err = analyze_factor(df_filtered, factor, metric)
            if err:
                report.append(f"\n- **{factor.capitalize()}**: {err}")
                continue
                
            p_val = res['overall_p']
            is_sig = p_val < 0.05
            report.append(f"\n#### 🔬 {factor.capitalize()}")
            report.append(f"**Prueba de Kruskal-Wallis (Global):**")
            report.append(f"- P-Value: `{p_val:.6f}`")
            report.append(f"- Diferencia Estadística: **{'SÍ' if is_sig else 'NO'}**")
            
            report.append("\n**Tabla de Rendimiento (Ranking):**")
            # Convertir dataframe a markdown
            sum_df = res['summary']
            report.append(sum_df[['Factor', 'Count', 'Mean', 'Median']].to_markdown(index=False))
            
            if is_sig and not res['posthoc'].empty:
                report.append("\n**Comparación con el mejor (Mann-Whitney U):**")
                report.append(res['posthoc'].to_markdown(index=False))
                
        # --- 2. Análisis de Combinación Completa ---
        report.append("\n### 🧩 Análisis de Combinación Completa")
        res_comb, err_comb = analyze_factor(df_filtered, 'Combination', metric)
        if err_comb:
            report.append(f"\n- **Combinación**: {err_comb}")
        else:
            p_val_comb = res_comb['overall_p']
            is_sig_comb = p_val_comb < 0.05
            report.append(f"**Prueba de Kruskal-Wallis (Global Combinatoria):**")
            report.append(f"- P-Value: `{p_val_comb:.6f}`")
            report.append(f"- Diferencias entre combinaciones: **{'SÍ' if is_sig_comb else 'NO'}**")
            
            report.append("\n**Top 5 Combinaciones (por Media):**")
            sum_df_comb = res_comb['summary'].head(5)
            report.append(sum_df_comb[['Factor', 'Count', 'Mean', 'Median']].to_markdown(index=False))
            
            if is_sig_comb and not res_comb['posthoc'].empty:
                report.append("\n**Combinaciones estadísticamente equivalentes al líder:**")
                leaders = res_comb['posthoc'][res_comb['posthoc']['Stat. Equal'] == 'Sí']
                if not leaders.empty:
                    report.append(leaders[['Other', 'p-value']].to_markdown(index=False))
                else:
                    report.append("_No hay otras combinaciones estadísticamente equivalentes al líder._")
                    
        report.append("\n" + "="*40 + "\n")
        
    final_report = "\n".join(report)
    
    # Guardar reporte
    out_path = os.path.join(output_dir, 'statistical_results.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(final_report)
        
    print(f"\n✅ Reporte generado exitosamente.")
    print(f"📄 Guardado en: {out_path}")
    print("\n--- Vista Previa del Reporte ---")
    print("\n".join(report[:30]))  # Mostrar primeros 30 líneas
    print("\n...")

if __name__ == "__main__":
    main()
