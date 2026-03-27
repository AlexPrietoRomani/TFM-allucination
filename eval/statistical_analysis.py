"""
statistical_analysis.py — Visualizador Estadístico de Rendimiento RAG

Ejecuta el pipeline de análisis estadístico (delegado a `stat_engine.py`) y
genera las visualizaciones de calidad de artículo científico:
  - Boxplots con letras CLD por cada métrica y factor.
  - Radar Charts (Spider plots) para las mejores combinaciones.

El cálculo estadístico puro (Kruskal-Wallis, ANOVA, Dunn, T-Test, CLD,
Mann-Whitney U) y la generación de CSVs/Markdown está en `stat_engine.py`,
que también es invocado por `run_matrix_eval.py` al final de cada evaluación.

Uso:
    uv run python eval/statistical_analysis.py

Salidas (`eval/results/Matrix/`):
    - statistical_factors_results.csv      : Métricas agregadas por componente individual.
    - statistical_combinations_results.csv : Métricas por combinación exacta (Pipeline).
    - best_factors_by_metric.csv           : Líderes estadísticos (Ganadores óptimos).
    - statistical_results.md               : Reporte Markdown detallado.
    - image/radar_top5_combinations.png    : Diagrama Radar para Top 5 combinaciones.
    - image/boxplot_[metrica].png          : Distribuciones por Generator y Architecture.
"""

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Asegurar que el directorio raíz esté en el PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from eval.stat_engine import run_statistical_analysis, PARAMETRIC_METRICS

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


# ── Mapa de etiquetas legibles ──────────────────────────────────────────────
LABEL_MAP = {
    'faithfulness_score':        'Faithfulness',
    'relevance_score':           'Context Relevance',
    'context_precision_score':   'Context Precision',
    'answer_relevancy_score':    'Answer Relevancy',
    'latency_retrieval_seg':     'Latency Retrieval (s)',
    'latency_generation_seg':    'Latency Generation (s)',
    'total_latency_seg':         'Total Latency (s)',
    'cost_est':                  'Cost (USD)',
    # Normalizados para Radar
    'latency_retrieval_seg_norm': 'Retrieval Lat. (Norm)',
    'latency_generation_seg_norm':'Gen. Lat. (Norm)',
    'total_latency_seg_norm':    'Total Lat. (Norm)',
    'cost_est_norm':             'Cost (Norm)',
}


def plot_radar_chart(df, metrics, title, save_path, group_col='Combination', top_n=5):
    """
    Genera un Radar Chart (spider plot) para las top N agrupaciones.
    Estilo: artículo científico (serif, blanco, paleta sobria).
    """
    grouped = df.groupby(group_col)[metrics].mean().reset_index()
    grouped['Overall_Score'] = grouped[metrics].mean(axis=1)
    top_items = grouped.sort_values(by='Overall_Score', ascending=False).head(top_n)

    categories = [LABEL_MAP.get(m, m.replace('_score', '').capitalize()) for m in metrics]
    N = len(categories)

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(9, 10), subplot_kw=dict(polar=True),
                           facecolor='white')
    ax.set_facecolor('white')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10, fontfamily='serif')
    ax.set_rlabel_position(30)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'],
                       color='#555555', fontsize=8)
    ax.set_ylim(0, 1.1)
    ax.spines['polar'].set_color('#cccccc')
    ax.grid(color='#cccccc', linestyle='--', linewidth=0.5, alpha=0.6)

    colors = ['#2c3e50', '#c0392b', '#2980b9', '#27ae60', '#8e44ad', 
              '#d35400', '#f39c12', '#16a085', '#34495e', '#7f8c8d']
    markers = ['o', 's', '^', 'D', 'v', 'p', '*', 'h', 'H', '+']

    for i, (_, row) in enumerate(top_items.iterrows()):
        values = row[metrics].tolist()
        values += values[:1]
        raw_label = str(row[group_col])
        label = f"({i+1}) {raw_label[:60]}{'...' if len(raw_label) > 60 else ''}"
        c_idx = i % len(colors)
        ax.plot(angles, values, linewidth=1.5, linestyle='-',
                marker=markers[c_idx], markersize=5,
                label=label, color=colors[c_idx])
        ax.fill(angles, values, alpha=0.08, color=colors[c_idx])

    ax.set_title(title, fontsize=14, fontfamily='serif',
                 fontweight='bold', pad=35)
    
    n_cols = 1 if top_n <= 5 else 2
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
             ncol=n_cols, frameon=True, fancybox=False,
             edgecolor='#cccccc', fontsize=9, title="Ranking de Desempeño", 
             title_fontsize=10)

    fig.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def plot_boxplots(df, metric, output_dir, metric_summaries_dict=None, is_parametric=False):
    """Genera boxplots con estilo de artículo científico para los 5 componentes principales."""
    metric_label = LABEL_MAP.get(metric, metric.replace('_score', '').capitalize())

    factors = [
        ('generator', 'Modelo Generador'),
        ('architecture', 'Arquitectura'),
        ('db_motor', 'Base de Datos Vectorial'),
        ('embedding', 'Modelo de Embedding'),
        ('chunk_strategy', 'Estrategia Chunking')
    ]

    # --- 1. Gráficos Individuales (uno por factor) ---
    for factor_col, factor_title in factors:
        fig_indiv, ax_indiv = plt.subplots(figsize=(7, 5), facecolor='white')
        
        ax_indiv.set_facecolor('white')
        ax_indiv.spines['top'].set_visible(False)
        ax_indiv.spines['right'].set_visible(False)
        ax_indiv.spines['left'].set_color('#333333')
        ax_indiv.spines['bottom'].set_color('#333333')
        ax_indiv.tick_params(colors='#333333')
        ax_indiv.yaxis.grid(True, linestyle='--', alpha=0.3, color='#999999')
        ax_indiv.xaxis.grid(False)

        order = sorted(df[factor_col].dropna().unique().tolist())
        sns.boxplot(x=factor_col, y=metric, data=df, ax=ax_indiv,
                    order=order, palette="Set2", linewidth=0.8, fliersize=3,
                    boxprops=dict(edgecolor='#333333'),
                    medianprops=dict(color='#333333', linewidth=1.5),
                    whiskerprops=dict(color='#333333'),
                    capprops=dict(color='#333333'))
        
        # Añadir letras CLD
        y_max_global = df[metric].max()
        y_min_global = df[metric].min()
        y_offset = (y_max_global - y_min_global) * 0.05 if y_max_global != y_min_global else 0.05
        
        if metric_summaries_dict and factor_col in metric_summaries_dict:
            summary_df = metric_summaries_dict[factor_col]
            if 'CLD_Letter' in summary_df.columns:
                for i, label in enumerate(order):
                    row = summary_df[summary_df['Factor_Value'] == label]
                    if not row.empty:
                        letter = row.iloc[0]['CLD_Letter']
                        group_max = df[df[factor_col] == label][metric].max()
                        ax_indiv.text(i, group_max + y_offset, letter, ha='center', va='bottom', 
                                      color='#333333', fontweight='heavy', fontsize=11, 
                                      fontstyle='italic', fontfamily='serif')

        ax_indiv.set_ylim(y_min_global - y_offset, y_max_global + y_offset * 3)
        
        ax_indiv.set_title(f'{metric_label} por {factor_title}',
                           fontfamily='serif', fontsize=13, fontweight='bold', pad=15)
        ax_indiv.set_xlabel(factor_title, fontfamily='serif', fontsize=11, labelpad=10)
        ax_indiv.set_ylabel(metric_label, fontfamily='serif', fontsize=11, labelpad=10)
        ax_indiv.set_xticklabels(ax_indiv.get_xticklabels(), rotation=30, ha='right', fontfamily='serif', fontsize=10)

        nota_tex = 'Nota: Letras distintas indican diferencias significativas (ANOVA + T-Test, p < 0.05).' if is_parametric else 'Nota: Letras distintas indican diferencias significativas (Kruskal-Wallis + Post-hoc de Dunn, p < 0.05).'
        fig_indiv.text(0.5, 0.01, nota_tex,
                       ha='center', fontsize=9, fontstyle='italic', color='#555555', fontfamily='serif')

        fig_indiv.tight_layout(rect=[0, 0.05, 1, 1])
        fig_indiv.savefig(os.path.join(output_dir, f'boxplot_{metric}_{factor_col}.png'),
                          dpi=300, bbox_inches='tight', facecolor='white')
        plt.close(fig_indiv)

    # --- 2. Gráfico Combinado (Junto) ---
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

        order = sorted(df[factor_col].dropna().unique().tolist())
        sns.boxplot(x=factor_col, y=metric, data=df, ax=ax,
                    order=order, palette="Set2", linewidth=0.8, fliersize=3,
                    boxprops=dict(edgecolor='#333333'),
                    medianprops=dict(color='#c0392b', linewidth=1.5),
                    whiskerprops=dict(color='#333333'),
                    capprops=dict(color='#333333'))
        
        # Añadir letras CLD
        y_max_global = df[metric].max()
        y_min_global = df[metric].min()
        y_offset = (y_max_global - y_min_global) * 0.05 if y_max_global != y_min_global else 0.05
        
        if metric_summaries_dict and factor_col in metric_summaries_dict:
            summary_df = metric_summaries_dict[factor_col]
            if 'CLD_Letter' in summary_df.columns:
                for j, label in enumerate(order):
                    row = summary_df[summary_df['Factor_Value'] == label]
                    if not row.empty:
                        letter = row.iloc[0]['CLD_Letter']
                        group_max = df[df[factor_col] == label][metric].max()
                        ax.text(j, group_max + y_offset, letter, ha='center', va='bottom', 
                                color='#333333', fontweight='heavy', fontsize=10, 
                                fontstyle='italic', fontfamily='serif')

        ax.set_ylim(y_min_global - y_offset, y_max_global + y_offset * 3)

        ax.set_title(f'{metric_label} por\n{factor_title}',
                     fontfamily='serif', fontsize=12, fontweight='bold')
        ax.set_xlabel(factor_title, fontfamily='serif', fontsize=10)
        ax.set_ylabel(metric_label, fontfamily='serif', fontsize=10)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

    fig.delaxes(axes[5])

    fig.tight_layout(pad=2.0, rect=[0, 0.06, 1, 1])
    nota_tex_comb = 'Nota: Letras distintas indican diferencias significativas (ANOVA + T-Test, p < 0.05).' if is_parametric else 'Nota: Letras distintas indican diferencias significativas (Kruskal-Wallis + Post-hoc de Dunn, p < 0.05).'
    fig.text(0.5, 0.015, nota_tex_comb,
             ha='center', fontsize=11, fontstyle='italic', color='#555555', fontfamily='serif')
    
    fig.savefig(os.path.join(output_dir, f'boxplot_{metric}.png'),
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close(fig)


def main():
    file_path = 'eval/results/Matrix/eval_results_matrix.jsonl'
    output_dir = 'eval/results/Matrix'
    image_dir = os.path.join(output_dir, 'image')
    os.makedirs(image_dir, exist_ok=True)

    target_models = ["deepseek-r1:8b", "qwen2.5:3b", "gpt-oss:20b"]

    # ── 1. Ejecutar análisis estadístico (CSVs + Markdown) ──────────────────
    result = run_statistical_analysis(file_path, output_dir, target_models)
    if result is None:
        return

    df = result['df']
    metrics = result['metrics']
    parametric_metrics = result['parametric_metrics']
    metric_summaries_by_metric = result['metric_summaries_by_metric']

    # ── 2. Generar Boxplots con letras CLD ──────────────────────────────────
    for metric in metrics:
        is_parametric = metric in parametric_metrics
        metric_summaries_dict = metric_summaries_by_metric.get(metric, {})
        plot_boxplots(df, metric, image_dir, metric_summaries_dict, is_parametric=is_parametric)

    # ── 3. Preparar Radar: normalización invertida para latencia/costo ──────
    df_radar = df.copy()
    radar_metrics = []
    for m in metrics:
        if m in parametric_metrics:
            min_val = df_radar[m].min()
            max_val = df_radar[m].max()
            norm_col = f"{m}_norm"
            if max_val > min_val:
                df_radar[norm_col] = 1.0 - (df_radar[m] - min_val) / (max_val - min_val)
            else:
                df_radar[norm_col] = 1.0
            radar_metrics.append(norm_col)
        else:
            radar_metrics.append(m)

    # ── 4. Generar Radar Charts ─────────────────────────────────────────────
    print("\n🕸️ Generando Radar Charts para visualización multidimensional...")
    plot_radar_chart(df_radar, radar_metrics, "Top 5 Combinaciones (Desempeño Global RAG)", 
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
        plot_radar_chart(df_radar, radar_metrics, f"Desempeño Global por {fact_title}", 
                         os.path.join(image_dir, f'radar_{fact_col}.png'), 
                         group_col=fact_col, top_n=10)

    print("\n🚀 Análisis estadístico e imágenes generadas completadas correctamente.")

if __name__ == "__main__":
    main()
