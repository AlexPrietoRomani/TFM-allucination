"""
stat_engine.py — Motor de Análisis Estadístico para Evaluación RAG

Contiene las funciones puras de análisis estadístico (Kruskal-Wallis, ANOVA,
Dunn, T-Test, Mann-Whitney U, CLD) utilizadas tanto por `run_matrix_eval.py`
(pipeline completo) como por `statistical_analysis.py` (solo visualización).

Pipeline No Paramétrico (métricas RAGAS [0,1]):
    Kruskal-Wallis → Dunn (FDR-BH) → Mann-Whitney U

Pipeline Paramétrico (latencia, costo):
    ANOVA → T-Test (FDR-BH) → T-Test pareado

Uso:
    from eval.stat_engine import analyze_factor, generate_markdown_report, run_statistical_analysis
"""

import pandas as pd
import json
import os
import numpy as np
from scipy.stats import kruskal, mannwhitneyu, f_oneway, ttest_ind
import scikit_posthocs as sp

# Métricas que reciben pipeline paramétrico (ANOVA + T-Test)
PARAMETRIC_METRICS = ['latency_retrieval_seg', 'latency_generation_seg', 'total_latency_seg', 'cost_est']

# Métricas RAGAS que reciben pipeline no paramétrico (Kruskal-Wallis + Dunn)
RAGAS_METRICS = ['faithfulness_score', 'relevance_score', 'context_precision_score', 'answer_relevancy_score']

# Factores de la matriz experimental
FACTORS = ['architecture', 'embedding', 'chunk_strategy', 'db_motor', 'generator']


def load_data(file_path):
    """Carga un archivo JSONL y retorna un DataFrame."""
    data = []
    bad_lines = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data.append(json.loads(line))
            except Exception:
                bad_lines += 1
    if bad_lines > 0:
        print(f"⚠️ Advertencia: {bad_lines} líneas corruptas omitidas en {file_path}")
    return pd.DataFrame(data)


def analyze_factor(df, factor_name, metric_name, is_parametric=False):
    """
    Ejecuta la prueba ómnibus (Kruskal-Wallis o ANOVA) y post-hoc (Dunn o T-Test)
    para un factor y métrica dados. Retorna un DataFrame con el ranking y CLD.
    """
    groups = []
    labels = []
    
    for val in df[factor_name].unique():
        series = df[df[factor_name] == val][metric_name].dropna()
        if len(series) >= 2:
            groups.append(series)
            labels.append(val)
            
    if len(groups) < 2:
        return None, f"Insuficientes grupos ({len(groups)})"

    try:
        if is_parametric:
            stat, p_val = f_oneway(*groups)
        else:
            stat, p_val = kruskal(*groups)
    except Exception as e:
        return None, str(e)
        
    summary = []
    for group, label in zip(groups, labels):
        summary.append({
            'Factor_Type': factor_name,
            'Factor_Value': str(label),
            'Metric': metric_name,
            'Count': len(group),
            'Mean': group.mean(),
            'Median': group.median(),
            'StdDev': group.std(),
            'Min': group.min(),
            'Max': group.max()
        })
        
    # Para paramétrico: menor es mejor (latencia/costo) → ascendente
    ascending_sort = True if is_parametric else False
    summary_df = pd.DataFrame(summary).sort_values(by='Mean', ascending=ascending_sort)
    
    # --- Post-Hoc & CLD ---
    try:
        tmp_df = df[[factor_name, metric_name]].dropna()
        if len(summary_df) > 1:
            if is_parametric:
                p_mat = sp.posthoc_ttest(tmp_df, val_col=metric_name, group_col=factor_name, p_adjust='fdr_bh')
            else:
                p_mat = sp.posthoc_dunn(tmp_df, val_col=metric_name, group_col=factor_name, p_adjust='fdr_bh')
            ordered_labels = summary_df['Factor_Value'].tolist()
            p_mat = p_mat.loc[ordered_labels, ordered_labels]
            
            from string import ascii_lowercase
            n = len(ordered_labels)
            letters = [''] * n
            current_letter_idx = 0
            for i in range(n):
                if not letters[i]:
                    letter = ascii_lowercase[current_letter_idx]
                    letters[i] += letter
                    current_letter_idx += 1
                    for j in range(i + 1, n):
                        can_share = True
                        for k in range(n):
                            if letter in letters[k]:
                                if p_mat.iloc[j, k] < 0.05:
                                    can_share = False
                                    break
                        if can_share:
                            letters[j] += letter
            summary_df['CLD_Letter'] = letters
        else:
            summary_df['CLD_Letter'] = ['a'] * len(summary_df)
    except Exception as e:
        summary_df['CLD_Letter'] = 'Error'
    
    # --- Comparación pairwise vs. Líder ---
    posthoc = []
    if len(summary_df) > 1:
        best_factor = summary_df.iloc[0]['Factor_Value']
        best_data = df[df[factor_name] == best_factor][metric_name].dropna()
        
        for i in range(len(summary_df)):
            other_factor = summary_df.iloc[i]['Factor_Value']
            if other_factor == best_factor:
                stat_eq = 'Líder'
                p_u = 1.0
            else:
                other_data = df[df[factor_name] == other_factor][metric_name].dropna()
                try:
                    if is_parametric:
                        stat_u, p_u = ttest_ind(best_data, other_data, alternative='two-sided')
                    else:
                        stat_u, p_u = mannwhitneyu(best_data, other_data, alternative='two-sided')
                    stat_eq = 'Sí' if p_u >= 0.05 else 'No'
                except:
                    p_u = np.nan
                    stat_eq = 'Error'
            posthoc.append({
                'Factor_Value': other_factor,
                'p_value_vs_best': p_u,
                'Stat_Equivalent_to_Best': stat_eq
            })
            
    if posthoc:
        ph_df = pd.DataFrame(posthoc)
        summary_df = summary_df.merge(ph_df, on='Factor_Value', how='left')
    else:
        summary_df['p_value_vs_best'] = np.nan
        summary_df['Stat_Equivalent_to_Best'] = 'Líder'

    summary_df['p_value_global'] = p_val
    return summary_df, None


def generate_markdown_report(final_df, metrics, factors, total_rows, target_models, output_file, parametric_metrics):
    """Genera un archivo Markdown con los resultados del análisis estadístico."""
    md_lines = [
        "# 📈 Informe de Análisis Estadístico del RAG",
        f"Modelos evaluados: {', '.join(target_models)}",
        f"Total registros analizados: {total_rows}",
        "",
        "---",
        ""
    ]
    
    for metric in metrics:
        metric_display = metric.replace('_score', '').upper()
        is_param = metric in parametric_metrics
        md_lines.extend([
            f"## 🎯 Métrica: `{metric_display}`",
            "",
            "### 🔍 Análisis por Factor Individual",
            ""
        ])
        
        # 1. Factores Individuales
        for factor in factors:
            factor_df = final_df[(final_df['Metric'] == metric) & (final_df['Factor_Type'] == factor)]
            if factor_df.empty: continue
            
            p_global = factor_df['p_value_global'].iloc[0]
            diff_stat = "**SÍ**" if p_global < 0.05 else "**NO**"
            test_name = "Prueba de ANOVA (Global):" if is_param else "Prueba de Kruskal-Wallis (Global):"
            
            md_lines.extend([
                f"#### 🔬 {factor.capitalize()}",
                f"**{test_name}**",
                f"- P-Value: `{p_global:.6f}`",
                f"- Diferencia Estadística: {diff_stat}",
                "",
                "**Tabla de Rendimiento (Ranking):**"
            ])
            
            # Tabla de Rendimiento
            if 'CLD_Letter' in factor_df.columns:
                ranking_df = factor_df[['Factor_Value', 'Count', 'Mean', 'Median', 'CLD_Letter']].copy()
            else:
                ranking_df = factor_df[['Factor_Value', 'Count', 'Mean', 'Median']].copy()
            ranking_df.rename(columns={'Factor_Value': 'Factor', 'CLD_Letter': 'CLD'}, inplace=True)
            md_lines.append(ranking_df.to_markdown(index=False))
            md_lines.append("")
            
            # Comparación con el mejor
            posthoc_df = factor_df[['Factor_Value', 'p_value_vs_best', 'Stat_Equivalent_to_Best']].copy()
            posthoc_df = posthoc_df[posthoc_df['Stat_Equivalent_to_Best'] != 'Líder']
            
            if not posthoc_df.empty:
                posthoc_df.rename(columns={'Factor_Value': 'Other', 'Stat_Equivalent_to_Best': 'Stat. Equal'}, inplace=True)
                md_lines.extend([
                    f"**Comparación con el mejor ({'T-Test' if is_param else 'Mann-Whitney U'}):**",
                    posthoc_df.to_markdown(index=False),
                    ""
                ])
                
        # 2. Combinación Completa
        comb_df = final_df[(final_df['Metric'] == metric) & (final_df['Factor_Type'] == 'Combination')]
        if not comb_df.empty:
            p_global = comb_df['p_value_global'].iloc[0]
            diff_stat = "**SÍ**" if p_global < 0.05 else "**NO**"
            test_name_comb = "Prueba de ANOVA (Global):" if is_param else "Prueba de Kruskal-Wallis (Global Combinatoria):"
            
            md_lines.extend([
                "### 🧩 Análisis de Combinación Completa",
                f"**{test_name_comb}**",
                f"- P-Value: `{p_global:.6f}`",
                f"- Diferencias entre combinaciones: {diff_stat}",
                "",
                "**Top 5 Combinaciones (por Media):**"
            ])
            
            if 'CLD_Letter' in comb_df.columns:
                top5_df = comb_df[['Factor_Value', 'Count', 'Mean', 'Median', 'CLD_Letter']].head(5).copy()
            else:
                top5_df = comb_df[['Factor_Value', 'Count', 'Mean', 'Median']].head(5).copy()
            top5_df.rename(columns={'Factor_Value': 'Factor', 'CLD_Letter': 'CLD'}, inplace=True)
            md_lines.append(top5_df.to_markdown(index=False))
            md_lines.append("")
            
            # Equivalentes
            equiv_df = comb_df[comb_df['Stat_Equivalent_to_Best'] == 'Sí'][['Factor_Value', 'p_value_vs_best']].copy()
            if not equiv_df.empty:
                equiv_df.rename(columns={'Factor_Value': 'Other'}, inplace=True)
                md_lines.extend([
                    "**Combinaciones estadísticamente equivalentes al líder:**",
                    equiv_df.to_markdown(index=False),
                    ""
                ])
                
        md_lines.extend(["========================================", ""])
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(md_lines))


def run_statistical_analysis(file_path, output_dir, target_models):
    """
    Ejecuta el pipeline completo de análisis estadístico:
    1. Carga datos JSONL
    2. Valida muestras (32 preguntas)
    3. Ejecuta pruebas ómnibus + post-hoc para cada métrica × factor
    4. Genera CSVs y reporte Markdown

    Retorna: (df, final_df, metrics, parametric_metrics, factors)
             para uso posterior en visualización.
    """
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(file_path):
        print(f"❌ Error: Archivo '{file_path}' no encontrado.")
        return None

    df = load_data(file_path)
    if df.empty:
        print("❌ Error: DataFrame vacío.")
        return None

    # Filtrar modelos
    df = df[df['generator'].isin(target_models)].copy()
    if df.empty:
        print("❌ Error: Ningún dato coincide con los modelos objetivo.")
        return None

    factors = FACTORS
    for f in factors:
        df[f] = df[f].fillna("N/A").astype(str)
    df['Combination'] = df.apply(lambda x: " | ".join([x[f] for f in factors]), axis=1)

    # VALIDACIÓN: 32 Preguntas por Combinación
    print("\n🔍 Validando conteo de preguntas por combinación...")
    combination_counts = df.groupby('Combination').size().reset_index(name='count')
    validations = []
    for _, row in combination_counts.iterrows():
        count = row['count']
        c = row['Combination']
        if count != 32:
            print(f"  ⚠️ Advertencia: La combinación '{c}' tiene {count}/32 pruebas.")
            validations.append({'Combination': c, 'Count': count, 'Status': 'Incompleto'})
        else:
            validations.append({'Combination': c, 'Count': count, 'Status': 'Completo'})
    val_df = pd.DataFrame(validations)
    val_df.to_csv(os.path.join(output_dir, 'validation_32_questions.csv'), index=False)
    print(f"📄 Resultado de validación guardado en validation_32_questions.csv")

    # Determinar métricas disponibles
    parametric_metrics = PARAMETRIC_METRICS
    metrics = [
        col for col in df.columns
        if (col.endswith('_score') and col in RAGAS_METRICS) or col in parametric_metrics
    ]

    for m in metrics:
        df[m] = pd.to_numeric(df[m], errors='coerce')

    # Análisis Estadístico Omnibus y Post-Hoc
    all_summaries = []
    metric_summaries_by_metric = {}  # {metric: {factor: summary_df}}

    for metric in metrics:
        print(f"📊 Analizando métrica: {metric} ...")
        is_parametric = metric in parametric_metrics
        metric_summaries_dict = {}

        # 1. Por factor individual
        for factor in factors:
            res, err = analyze_factor(df, factor, metric, is_parametric=is_parametric)
            if res is not None:
                all_summaries.append(res)
                metric_summaries_dict[factor] = res

        # 2. Por combinación completa
        res_comb, err = analyze_factor(df, 'Combination', metric, is_parametric=is_parametric)
        if res_comb is not None:
            all_summaries.append(res_comb)

        metric_summaries_by_metric[metric] = metric_summaries_dict

    # Concatenar y guardar CSVs
    final_df = None
    if all_summaries:
        final_df = pd.concat(all_summaries, ignore_index=True)

        factor_results = final_df[final_df['Factor_Type'] != 'Combination']
        comb_results = final_df[final_df['Factor_Type'] == 'Combination']

        factor_csv = os.path.join(output_dir, 'statistical_factors_results.csv')
        comb_csv = os.path.join(output_dir, 'statistical_combinations_results.csv')

        factor_results.to_csv(factor_csv, index=False, encoding='utf-8-sig')
        comb_results.to_csv(comb_csv, index=False, encoding='utf-8-sig')

        print("\n✅ Archivos CSV generados:")
        print(f"   - {factor_csv}")
        print(f"   - {comb_csv}")

        # Obtener el MEJOR por cada factor y métrica
        best_df = factor_results[factor_results['Stat_Equivalent_to_Best'] == 'Líder'].copy()
        best_df = best_df[['Factor_Type', 'Factor_Value', 'Metric', 'Mean', 'Median']]
        best_csv = os.path.join(output_dir, 'best_factors_by_metric.csv')
        best_df.to_csv(best_csv, index=False, encoding='utf-8-sig')
        print(f"   - {best_csv}")

        # Generar Reporte Markdown
        md_file = os.path.join(output_dir, 'statistical_results.md')
        generate_markdown_report(final_df, metrics, factors, len(df), target_models, md_file, parametric_metrics)
        print(f"   - {md_file}")

    return {
        'df': df,
        'final_df': final_df,
        'metrics': metrics,
        'parametric_metrics': parametric_metrics,
        'factors': factors,
        'metric_summaries_by_metric': metric_summaries_by_metric,
        'target_models': target_models,
    }
