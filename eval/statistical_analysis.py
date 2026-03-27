"""
statistical_analysis.py — Analizador Estadístico de Rendimiento RAG

Carga los resultados matriciales de `eval_results_matrix.jsonl`, filtra por
modelos objetivo y ejecuta pruebas estadísticas (Kruskal-Wallis y Mann-Whitney U)
para determinar qué componentes (Arquitectura, Embedding, Chunking, DB, Generador)
ofrecen el rendimiento óptimo y libre de alucinaciones.

Uso:
    uv run python eval/statistical_analysis.py

Funcionalidades:
    - Valida muestra de tests (32 preguntas por combinación).
    - Analiza métricas RAGAS (Faithfulness, Relevance, Context Precision, etc.).
    - Identifica líderes estadísticos por factor individual y combinación completa.
    - Genera diagramas Radar (Spider charts) y Boxplots de distribuciones.

Salidas (`eval/results/Matrix/`):
    - statistical_factors_results.csv      : Métricas agregadas por componente individual.
    - statistical_combinations_results.csv : Métricas por combinación exacta (Pipeline).
    - best_factors_by_metric.csv           : Líderes estadísticos (Ganadores óptimos).
    - image/radar_top5_combinations.png   : Diagrama Radar para Top 5 combinaciones.
    - image/boxplot_[metrica].png          : Distribuciones por Generator y Architecture.
"""

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

# ── Estilo global: formato artículo científico ──────────────────────────────
plt.rcParams.update({
    'font.family':        'serif',
    'font.serif':         ['Times New Roman', 'DejaVu Serif', 'serif'],
    'font.size':          11,
    'axes.titlesize':     13,
    'axes.labelsize':     11,
    'xtick.labelsize':    9,
    'ytick.labelsize':    9,
    'legend.fontsize':    9,
    'figure.titlesize':   14,
    'axes.edgecolor':     '#333333',
    'axes.linewidth':     0.8,
    'axes.grid':          True,
    'grid.alpha':         0.3,
    'grid.linestyle':     '--',
    'figure.facecolor':   'white',
    'axes.facecolor':     'white',
    'savefig.facecolor':  'white',
    'savefig.dpi':        300,
    'savefig.bbox':       'tight',
})
sns.set_style('whitegrid', {'grid.linestyle': '--', 'grid.alpha': 0.3})

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

def plot_radar_chart(df, metrics, title, save_path, group_col='Combination', top_n=5):
    """
    Genera un Radar Chart (spider plot) para las top N agrupaciones.
    Estilo: artículo científico (serif, blanco, paleta sobria).
    """
    LABEL_MAP = {
        'faithfulness_score':        'Faithfulness',
        'relevance_score':           'Context Relevance',
        'context_precision_score':   'Context Precision',
        'answer_relevancy_score':    'Answer Relevancy',
    }

    grouped = df.groupby(group_col)[metrics].mean().reset_index()
    grouped['Overall_Score'] = grouped[metrics].mean(axis=1)
    top_items = grouped.sort_values(by='Overall_Score', ascending=False).head(top_n)

    categories = [LABEL_MAP.get(m, m.replace('_score', '').capitalize()) for m in metrics]
    N = len(categories)

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 7), subplot_kw=dict(polar=True),
                           facecolor='white')
    ax.set_facecolor('white')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, fontfamily='serif')
    ax.set_rlabel_position(30)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'],
                       color='#555555', fontsize=8)
    ax.set_ylim(0, 1)
    ax.spines['polar'].set_color('#cccccc')
    ax.grid(color='#cccccc', linestyle='--', linewidth=0.5, alpha=0.6)

    # Paleta extendida para publicación científica
    colors = ['#2c3e50', '#c0392b', '#2980b9', '#27ae60', '#8e44ad', 
              '#d35400', '#f39c12', '#16a085', '#34495e', '#7f8c8d']
    markers = ['o', 's', '^', 'D', 'v', 'p', '*', 'h', 'H', '+']

    for i, (_, row) in enumerate(top_items.iterrows()):
        values = row[metrics].tolist()
        values += values[:1]
        raw_label = str(row[group_col])
        label = f"({i+1}) {raw_label[:45]}"
        c_idx = i % len(colors)
        ax.plot(angles, values, linewidth=1.5, linestyle='-',
                marker=markers[c_idx], markersize=4,
                label=label, color=colors[c_idx])
        ax.fill(angles, values, alpha=0.06, color=colors[c_idx])

    ax.set_title(title, fontsize=13, fontfamily='serif',
                 fontweight='bold', pad=25)
    ax.legend(loc='upper left', bbox_to_anchor=(-0.25, -0.08),
             ncol=1, frameon=True, fancybox=False,
             edgecolor='#cccccc', fontsize=8)

    fig.tight_layout()
    fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)

def plot_boxplots(df, metric, output_dir):
    """Genera boxplots con estilo de artículo científico para los 5 componentes principales."""
    LABEL_MAP = {
        'faithfulness_score':        'Faithfulness',
        'relevance_score':           'Context Relevance',
        'context_precision_score':   'Context Precision',
        'answer_relevancy_score':    'Answer Relevancy',
    }
    metric_label = LABEL_MAP.get(metric, metric.replace('_score', '').capitalize())

    factors = [
        ('generator', 'Modelo Generador'),
        ('architecture', 'Arquitectura'),
        ('db_motor', 'Base de Datos Vectorial'),
        ('embedding', 'Modelo de Embedding'),
        ('chunk_strategy', 'Estrategia Chunking')
    ]

    fig, axes = plt.subplots(2, 3, figsize=(16, 10), facecolor='white')
    axes = axes.flatten()

    for i, (factor_col, factor_title) in enumerate(factors):
        ax = axes[i]
        ax.set_facecolor('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color('#333333')
        ax.spines['bottom'].set_color('#333333')
        ax.tick_params(colors='#333333')
        ax.yaxis.grid(True, linestyle='--', alpha=0.3, color='#999999')
        ax.xaxis.grid(False)

        # Paleta sobria ("Set2" de seaborn o paleta por defecto)
        sns.boxplot(x=factor_col, y=metric, data=df, ax=ax,
                    palette="Set2", linewidth=0.8, fliersize=3,
                    boxprops=dict(edgecolor='#333333'),
                    medianprops=dict(color='#c0392b', linewidth=1.5),
                    whiskerprops=dict(color='#333333'),
                    capprops=dict(color='#333333'))
        
        ax.set_title(f'{metric_label} por\n{factor_title}',
                     fontfamily='serif', fontsize=12, fontweight='bold')
        ax.set_xlabel(factor_title, fontfamily='serif', fontsize=10)
        ax.set_ylabel(metric_label, fontfamily='serif', fontsize=10)
        
        # Rotar etiquetas para que encajen mejor
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    # Ocultar el sexto subplot que queda vacío
    fig.delaxes(axes[5])

    fig.tight_layout(pad=2.0)
    fig.savefig(os.path.join(output_dir, f'boxplot_{metric}.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)

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

    # 4 métricas RAGAS finales (FactScore descartada — ver docs/METRICAS_IMPLEMENTADAS.md §5)
    metrics = [
        col for col in df.columns 
        if col.endswith('_score') and col in [
            'faithfulness_score',
            'relevance_score',
            'context_precision_score',
            'answer_relevancy_score',
        ]
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
    plot_radar_chart(df, metrics, "Top 5 Combinaciones (Desempeño Global RAG)", 
                     os.path.join(image_dir, 'radar_top5_combinations.png'), 
                     group_col='Combination', top_n=5)
    
    radar_factors = [
        ('architecture', 'Arquitectura'),
        ('db_motor', 'Base de Datos Vectorial'),
        ('embedding', 'Modelo de Embedding'),
        ('chunk_strategy', 'Estrategia Chunking'),
        ('generator', 'Modelo Generador')
    ]
    
    for fact_col, fact_title in radar_factors:
        plot_radar_chart(df, metrics, f"Desempeño Global por {fact_title}", 
                         os.path.join(image_dir, f'radar_{fact_col}.png'), 
                         group_col=fact_col, top_n=10)

    print("\n🚀 Análisis estadístico e imágenes generadas completadas correctamente.")

if __name__ == "__main__":
    main()
