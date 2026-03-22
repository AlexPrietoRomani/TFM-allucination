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

    # --- 🛠️ 1. LANZAR EVALUACIÓN DESDE LA UI ---
    with st.expander("▶️ Iniciar Evaluación / Ejecutar Benchmark", expanded=False):
        st.markdown("Configura los parámetros para correr `eval/run_matrix_eval.py` desde esta interfaz:")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            sel_emb = st.selectbox("Embedding", ["Cualquiera", "mxbai-embed-large", "nomic-embed-text-v2-moe", "qwen3-embedding"])
            sel_chunk = st.selectbox("Fragmentación (Chunking)", ["Cualquiera", "500", "1000", "semantic"])
        with c2:
            sel_db = st.selectbox("Motor DB", ["Cualquiera", "faiss", "qdrant_local"])
            sel_gen = st.selectbox("Generador", ["Cualquiera", "gemini-3.1-pro-preview", "gemini-3-flash-preview", "gemini-3.1-flash-lite-preview", "deepseek-r1:8b", "qwen3:8b", "gpt-oss:20b"])
        with c3:
            sel_arch = st.selectbox("Arquitectura", ["Cualquiera", "v0", "v1", "v2"])
            limit_q = st.number_input("Límite de Preguntas (0 = Todas)", min_value=0, max_value=128, value=1)
            
        overwrite_check = st.checkbox("Sobrescribir Resultados previos para esta combinación (--overwrite)", value=False)
        
        # 1. Construir Comando (Fuera del botón para que sea visible siempre)
        args_list = []
        if sel_emb != "Cualquiera": args_list.append(f"--embedding {sel_emb}")
        if sel_chunk != "Cualquiera": args_list.append(f"--chunk-strategy {sel_chunk}")
        if sel_db != "Cualquiera": args_list.append(f"--db-motor {sel_db}")
        if sel_gen != "Cualquiera": args_list.append(f"--generator {sel_gen}")
        if sel_arch != "Cualquiera": args_list.append(f"--architecture {sel_arch}")
        if limit_q > 0: args_list.append(f"--limit {limit_q}")
        if overwrite_check: args_list.append("--overwrite")
        
        cmd = f"uv run python eval/run_matrix_eval.py " + " ".join(args_list)

        st.markdown("📋 **Comando de Consola Generado:**")
        st.code(cmd, language="bash")
        
        if st.button("🚀 Iniciar Ejecución en Background"):
            import subprocess
            
            log_area = st.empty()
            full_log = ""
            
            try:
                import os
                # Forzar encoding UTF-8 para evitar caídas en Windows Subprocess (Especialmente Emojis)
                env_exec = {**os.environ, "PYTHONIOENCODING": "utf-8"}
                
                # Abrir subprocess leyendo stdout en tiempo real
                p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, env=env_exec)
                for line in p.stdout:
                    full_log += line
                    # Limitar un poco el buffer si es muy masivo
                    log_area.code(full_log[-10000:])
                p.wait()
                if p.returncode == 0:
                    st.success("✅ Evaluación Completada con Éxito. Los gráficos se actualizarán al recargar o filtrar.")
                else:
                    st.error(f"❌ Falló con código {p.returncode}")
            except Exception as e:
                st.error(f"⚠️ Error al lanzar el proceso: {e}")

    st.divider()

    df = load_data()

    if df is None or df.empty:
        st.info("⚠️ **No se encontraron datos de evaluación de matriz.**")
        st.markdown(
            """
            Para generar datos, puedes expandir el bloque de arriba y configurar una corrida.
            """
        )
        return

    # --- Filtros de Datos ---
    st.sidebar.markdown("---")
    st.sidebar.markdown("🎯 **Filtros de Matriz**")
    
    # 1. Embedding
    embeddings_list = ["Todos"] + list(df['embedding'].unique() if 'embedding' in df.columns else [])
    sel_emb_filter = st.sidebar.selectbox("Filtrar Embedding", embeddings_list, index=0)

    # 2. Chunk Strategy
    chunks_list = ["Todos"] + list(df['chunk_strategy'].astype(str).unique() if 'chunk_strategy' in df.columns else [])
    sel_chunk_filter = st.sidebar.selectbox("Filtrar Chunking", chunks_list, index=0)

    # 3. Motor DB
    dbs_list = ["Todos"] + list(df['db_motor'].unique() if 'db_motor' in df.columns else [])
    sel_db_filter = st.sidebar.selectbox("Filtrar Motor DB", dbs_list, index=0)

    # 4. Generador
    generators_list = ["Todos"] + list(df['generator'].unique() if 'generator' in df.columns else [])
    selected_gen = st.sidebar.selectbox("Filtrar Generador", generators_list, index=0)

    # 5. Arquitectura
    architectures_list = ["Todos"] + list(df['architecture'].unique() if 'architecture' in df.columns else [])
    selected_arch = st.sidebar.selectbox("Filtrar Arquitectura", architectures_list, index=0)

    # Aplicar Filtrado
    filtered_df = df.copy()
    if 'embedding' in filtered_df.columns and sel_emb_filter != "Todos":
        filtered_df = filtered_df[filtered_df['embedding'] == sel_emb_filter]
        
    if 'chunk_strategy' in filtered_df.columns and sel_chunk_filter != "Todos":
        filtered_df = filtered_df[filtered_df['chunk_strategy'].astype(str) == sel_chunk_filter]
        
    if 'db_motor' in filtered_df.columns and sel_db_filter != "Todos":
        filtered_df = filtered_df[filtered_df['db_motor'] == sel_db_filter]
        
    if 'generator' in filtered_df.columns and selected_gen != "Todos":
        filtered_df = filtered_df[filtered_df['generator'] == selected_gen]
        
    if 'architecture' in filtered_df.columns and selected_arch != "Todos":
        filtered_df = filtered_df[filtered_df['architecture'] == selected_arch]

    # --- KPI Overview ---
    metrics_list = ["faithfulness_score", "relevance_score", "context_precision_score", "answer_relevancy_score", "factscore_score"]
    available_top_metrics = [m for m in metrics_list if m in filtered_df.columns]

    kpi_values = {m: filtered_df[m].mean() for m in available_top_metrics}
    avg_latency = filtered_df['total_latency_seg'].mean()

    labels_map = {
        "faithfulness_score": "Fidelidad",
        "relevance_score": "Rel. Contexto",
        "context_precision_score": "Prec. Contexto",
        "answer_relevancy_score": "Rel. Respuesta",
        "factscore_score": "FactScore"
    }

    cols = st.columns(len(available_top_metrics) + 1)
    for i, m in enumerate(available_top_metrics):
        cols[i].metric(labels_map.get(m, m), f"{kpi_values[m]:.2f}")
    cols[-1].metric("Latencia", f"{avg_latency:.2f} s")

    st.divider()

    # --- DATA TABLE & EXPORT ---
    st.markdown("### 📋 Tabla de Resultados")
    
    st.write("🔍 **Sub-filtros Avanzados para la Tabla**")
    cols_to_filter = st.multiselect(
        "Filtrar contenido de columnas específicas:", 
        ["question_id", "generator", "embedding", "chunk_strategy", "db_motor", "architecture"], 
        default=[], 
        key="adv_tbl_filters"
    )
    
    table_filtered_df = filtered_df.copy()
    
    if cols_to_filter:
        st.info("💡 Desmarca valores en las columnas inferiores para reducir las filas de la tabla.")
        cols_grid = st.columns(len(cols_to_filter))
        for i, col in enumerate(cols_to_filter):
            with cols_grid[i]:
                if col in table_filtered_df.columns:
                    unique_vals = sorted(list(table_filtered_df[col].astype(str).unique()))
                    selected_vals = st.multiselect(f"Filtrar {col.capitalize()}", unique_vals, default=unique_vals, key=f"f_sub_{col}")
                    table_filtered_df = table_filtered_df[table_filtered_df[col].astype(str).isin(selected_vals)]

    st.markdown("---")
    st.write("🔧 **Opciones de Agrupación**")
    group_cols = st.multiselect("Promediar métricas agrupando por:", ["architecture", "generator", "embedding", "chunk_strategy", "db_motor"], default=[], key="table_group_cols")

    table_base = ["question_id", "generator", "embedding", "chunk_strategy", "db_motor", "total_latency_seg"]
    if 'architecture' in filtered_df.columns:
        table_base.insert(2, "architecture")
    table_cols = table_base + available_top_metrics

    # Vista agrupada o vista plana sobre el dataframe filtrado
    if group_cols:
        numeric_cols = available_top_metrics + ["total_latency_seg"]
        df_grouped = table_filtered_df.groupby(group_cols)[numeric_cols].mean().reset_index()
        st.dataframe(df_grouped, use_container_width=True)
    else:
        st.dataframe(table_filtered_df[table_cols], use_container_width=True)

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
        st.write("#### 📦 Distribución de Métricas por Estrategia")
        
        metrics_dict = {
            "faithfulness_score": {
                "label": "Fidelidad (Faithfulness)",
                "desc": "Evalúa si la respuesta del asistente se basa estrictamente en el contexto proporcionado, penalizando información inventada o alucinaciones."
            },
            "relevance_score": {
                "label": "Relevancia del Contexto (Context Relevance)",
                "desc": "Mide qué tan útil y pertinente fue la información recuperada de la base de datos para responder a la pregunta."
            },
            "context_precision_score": {
                "label": "Precisión del Contexto (Context Precision)",
                "desc": "Analiza si la información crucial del contexto recuperado está en las primeras posiciones de los resultados de búsqueda."
            },
            "answer_relevancy_score": {
                "label": "Relevancia de la Respuesta (Answer Relevancy)",
                "desc": "Evalúa si la respuesta generada por el LLM responde directamente y de forma completa a la pregunta original."
            },
            "factscore_score": {
                "label": "FactScore",
                "desc": "Cuantifica la proporción de afirmaciones atómicas (hechos individuales) en la respuesta que están sustentados rigurosamente por el contexto."
            }
        }

        # Filtrar métricas por si alguna no está en el dataframe
        available_metrics = {k: v for k, v in metrics_dict.items() if k in filtered_df.columns}
        
        selected_metric_key = st.selectbox(
            "Seleccionar Métrica de Evaluación",
            options=list(available_metrics.keys()),
            format_func=lambda x: available_metrics[x]["label"]
        )
        
        selected_metric = available_metrics[selected_metric_key]
        st.info(f"💡 **Explicación:** {selected_metric['desc']}")
        
        st.markdown("---")
        st.write("🔧 **Configuración de Agrupación para el Gráfico**")
        c_box1, c_box2 = st.columns(2)
        with c_box1:
            group_x = st.selectbox("Eje X (Agrupar por)", ["embedding", "chunk_strategy", "db_motor", "generator", "architecture"], index=0, key="box_grp_x")
        with c_box2:
            group_color = st.selectbox("Color (Separar por)", ["chunk_strategy", "embedding", "db_motor", "generator", "architecture"], index=0, key="box_grp_hue")

        fig_box = px.box(
            filtered_df, 
            x=group_x, 
            y=selected_metric_key, 
            color=group_color,
            points="all",
            labels={group_x: group_x.capitalize(), selected_metric_key: f"{selected_metric['label']}"},
            title=f"Distribución de {selected_metric['label']} vs {group_x.upper()} (Agrupado por {group_color.upper()})"
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
