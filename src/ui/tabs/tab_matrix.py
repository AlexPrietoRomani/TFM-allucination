import streamlit as st
import pandas as pd
import json
from pathlib import Path
import plotly.express as px

RESULTS_FILE = Path("eval/results/Matrix/eval_results_matrix.jsonl")

def load_data():
    """Carga los resultados .jsonl a un DataFrame."""
    if not RESULTS_FILE.exists():
        return None
    
    data = []
    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return pd.DataFrame(data)

def render_tab_matrix():
    """Renderiza la pestaña de la Matriz de Experimentos."""
    st.subheader("📊 Matriz de Experimentos")
    st.caption("_Resultados de las 27 permutaciones evaluando el impacto de Embedding, Chunking y DB en la respuesta RAG._")

    # Banner de Juez Estático
    st.warning("⚖️ **Juez Evaluador Único:** `llama3.1` (Ollama)")

    df = load_data()

    if df is None or df.empty:
        st.info("⚠️ **No se encontraron datos de evaluación de matriz.**")
        st.markdown(
            """
            Para generar datos, sigue estos pasos en la terminal:
            1. `$env:PYTHONPATH="."; python scripts/build_vector_matrix.py` *(Construye las bases de datos)*
            2. `$env:PYTHONPATH="."; python eval/run_matrix_eval.py --limit 3` *(Corre la evaluación en un subset rápido)*
            """
        )
        return

    # --- Filtros de Datos ---
    st.sidebar.markdown("---")
    st.sidebar.markdown("🎯 **Filtros de Matriz**")
    generators = ["Todos"] + list(df['generator'].unique())
    selected_gen = st.sidebar.selectbox("Seleccionar Generador", generators, index=0)

    # Filtrado
    filtered_df = df.copy()
    if selected_gen != "Todos":
        filtered_df = filtered_df[filtered_df['generator'] == selected_gen]

    # --- KPI Overview ---
    avg_faith = filtered_df['faithfulness_score'].mean()
    avg_rel = filtered_df['relevance_score'].mean()
    avg_latency = filtered_df['total_latency_seg'].mean()

    c1, c2, c3 = st.columns(3)
    c1.metric("Fidelidad Promedio (Faithfulness)", f"{avg_faith:.2f}")
    c2.metric("Relevancia Promedio (Context)", f"{avg_rel:.2f}")
    c3.metric("Latencia Promedio (Ret + Gen)", f"{avg_latency:.2f} s")

    st.divider()

    # --- DATA TABLE & EXPORT ---
    st.markdown("### 📋 Tabla de Resultados")
    st.dataframe(filtered_df[[
        "question_id", "generator", "embedding", "chunk_strategy", "db_motor", 
        "faithfulness_score", "relevance_score", "total_latency_seg"
    ]], use_container_width=True)

    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Resultados en CSV",
        data=csv,
        file_name='tfm_matriz_resultados.csv',
        mime='text/csv',
    )

    st.divider()

    # --- GRÁFICOS ---
    st.markdown("### 📈 Análisis y Gráficas")

    tab_box, tab_pareto, tab_latency = st.tabs([
        "📦 Distribución (Boxplots)", "🎯 Frontera de Pareto", "⏱️ Desglose de Latencia"
    ])

    with tab_box:
        st.write("#### 📦 Distribución de Fidelidad por Estrategia")
        fig_box = px.box(
            filtered_df, 
            x="embedding", 
            y="faithfulness_score", 
            color="chunk_strategy",
            points="all",
            labels={"embedding": "Modelo de Embedding", "faithfulness_score": "Puntuación de Fidelidad"},
            title="Fidelidad vs Embedding y Tamaño de Chunk"
        )
        st.plotly_chart(fig_box, use_container_width=True)

    with tab_pareto:
         st.write("#### 🎯 Eficiencia: Latencia vs Fidelidad")
         fig_scatter = px.scatter(
             filtered_df,
             x="total_latency_seg",
             y="faithfulness_score",
             color="embedding",
             size=[10] * len(filtered_df),
             hover_data=["generator", "chunk_strategy", "db_motor", "question_id"],
             labels={"total_latency_seg": "Latencia Total (Segundos)", "faithfulness_score": "Fidelidad (0.0 - 1.0)"},
             title="Frontera de Pareto: Latencia vs Calidad"
         )
         st.plotly_chart(fig_scatter, use_container_width=True)

    with tab_latency:
         st.write("#### ⏱️ Latencia: Recuperación vs Generación")
         # Agrupar datos para promedio por combinacion para simplicidad
         agg_df = filtered_df.groupby(["embedding", "chunk_strategy", "db_motor"]).agg({
             "latency_retrieval_seg": "mean",
             "latency_generation_seg": "mean"
         }).reset_index()

         agg_df["comb_id"] = agg_df["embedding"] + " - " + agg_df["chunk_strategy"] + " (" + agg_df["db_motor"] + ")"

         fig_bar = px.bar(
             agg_df,
             x="comb_id",
             y=["latency_retrieval_seg", "latency_generation_seg"],
             title="Tiempo de Index/Búsqueda vs Generación (Promedios)",
             labels={"value": "Segundos", "comb_id": "Combinación"},
             barmode="stack"
         )
         st.plotly_chart(fig_bar, use_container_width=True)
