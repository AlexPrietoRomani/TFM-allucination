import pandas as pd
import json
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal, mannwhitneyu
import warnings

# Ignorar warnings de seaborn/matplotlib que puedan ensuciar la consola
warnings.filterwarnings('ignore')

def load_data(file_path):
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

def analyze_factor(df, factor_name, metric_name):
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
        
    summary_df = pd.DataFrame(summary).sort_values(by='Mean', ascending=False)
    
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
            
    # Hacemos merge
    if posthoc:
        ph_df = pd.DataFrame(posthoc)
        summary_df = summary_df.merge(ph_df, on='Factor_Value', how='left')
    else:
        summary_df['p_value_vs_best'] = np.nan
        summary_df['Stat_Equivalent_to_Best'] = 'Líder'

    summary_df['Kruskal_p_value_global'] = p_val
    return summary_df, None

def plot_radar_chart(df, metrics, title, save_path):
    """
    Genera un Radar Chart (spider plot) para las top 5 combinaciones.
    Recomendado en literatura de LLM metrics benchmarking para visualización multidimensional.
    """
    # Tomamos el promedio por combinación para cada métrica
    grouped = df.groupby('Combination')[metrics].mean().reset_index()
    
    # Ordenar por una métrica agregada simple para sacar las Top 5
    grouped['Overall_Score'] = grouped[metrics].mean(axis=1)
    top5 = grouped.sort_values(by='Overall_Score', ascending=False).head(5)
    
    categories = [m.replace('_score', '').capitalize() for m in metrics]
    N = len(categories)
    
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(polar=True))
    
    plt.xticks(angles[:-1], categories, size=12, fontweight='bold')
    ax.set_rlabel_position(0)
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.2","0.4","0.6","0.8","1.0"], color="grey", size=10)
    plt.ylim(0, 1)

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    for i, (_, row) in enumerate(top5.iterrows()):
        values = row[metrics].tolist()
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=f"Rank {i+1}: {row['Combination'][:40]}...", color=colors[i])
        ax.fill(angles, values, alpha=0.1, color=colors[i])

    plt.title(title, size=16, fontweight='bold', y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()

def plot_boxplots(df, metric, output_dir):
    """Genera boxplots para distribution de métricas por Generator y Architecture"""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    sns.boxplot(x='generator', y=metric, data=df, ax=axes[0], palette="Set2")
    axes[0].set_title(f'Distribución de {metric.replace("_score","").capitalize()} por Generator')
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45)
    
    sns.boxplot(x='architecture', y=metric, data=df, ax=axes[1], palette="Set3")
    axes[1].set_title(f'Distribución de {metric.replace("_score","").capitalize()} por Architecture')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f'boxplot_{metric}.png'), dpi=300, bbox_inches='tight')
    plt.close()

def main():
    file_path = 'eval/results/Matrix/eval_results_matrix.jsonl'
    output_dir = 'eval/results/Matrix'
    image_dir = os.path.join(output_dir, 'image')
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(image_dir, exist_ok=True)
    
    if not os.path.exists(file_path):
        print(f"❌ Error: Archivo '{file_path}' no encontrado.")
        return
        
    df = load_data(file_path)
    if df.empty:
        print("❌ Error: DataFrame vacío.")
        return
        
    # Filtrar modelos
    target_models = ["deepseek-r1:8b", "qwen2.5:3b", "gpt-oss:20b"]
    df = df[df['generator'].isin(target_models)].copy()
    
    if df.empty:
        print("❌ Error: Ningún dato coincide con los modelos objetivo.")
        return
        
    # Crear Combinación
    factors = ['architecture', 'embedding', 'chunk_strategy', 'db_motor', 'generator']
    
    # Manejar "N/A" convirtiéndolos en strings si fuera necesario, para que combinen bien
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

    metrics = [
        col for col in df.columns 
        if col.endswith('_score') and col in ['faithfulness_score', 'relevance_score', 'context_precision_score', 'answer_relevancy_score', 'factscore_score']
    ]
    
    for m in metrics:
        df[m] = pd.to_numeric(df[m], errors='coerce')
        
    # Análisis Estadístico Kruskal-Wallis y Mann-Whitney U
    all_summaries = []
    
    for metric in metrics:
        print(f"📊 Analizando métrica: {metric} ...")
        
        # Generar Gráficos Boxplot
        plot_boxplots(df, metric, image_dir)
        
        # 1. Por factor individual
        for factor in factors:
            res, err = analyze_factor(df, factor, metric)
            if res is not None:
                all_summaries.append(res)
                
        # 2. Por combinación completa
        res_comb, err = analyze_factor(df, 'Combination', metric)
        if res_comb is not None:
            all_summaries.append(res_comb)
            
    # Concatenar todos los resultados y guardar en DataFrames detallados
    if all_summaries:
        final_df = pd.concat(all_summaries, ignore_index=True)
        
        # Separar factores individuales y combinaciones
        factor_df = final_df[final_df['Factor_Type'] != 'Combination']
        comb_df = final_df[final_df['Factor_Type'] == 'Combination']
        
        factor_csv = os.path.join(output_dir, 'statistical_factors_results.csv')
        comb_csv = os.path.join(output_dir, 'statistical_combinations_results.csv')
        
        factor_df.to_csv(factor_csv, index=False, encoding='utf-8-sig')
        comb_df.to_csv(comb_csv, index=False, encoding='utf-8-sig')
        
        print("\n✅ Archivos CSV generados:")
        print(f"   - {factor_csv}")
        print(f"   - {comb_csv}")
        
        # Obtener el MEJOR por cada factor y métrica
        best_df = factor_df[factor_df['Stat_Equivalent_to_Best'] == 'Líder'].copy()
        best_df = best_df[['Factor_Type', 'Factor_Value', 'Metric', 'Mean', 'Median']]
        best_csv = os.path.join(output_dir, 'best_factors_by_metric.csv')
        best_df.to_csv(best_csv, index=False, encoding='utf-8-sig')
        print(f"   - {best_csv}")
        
    # Gráficos de Radar
    print("\n🕸️ Generando Radar Charts para visualización multidimensional...")
    plot_radar_chart(df, metrics, "Top 5 Combinaciones (Desempeño Global RAG)", os.path.join(image_dir, 'radar_top5_combinations.png'))

    print("\n🚀 Análisis estadístico e imágenes generadas completadas correctamente.")

if __name__ == "__main__":
    main()
