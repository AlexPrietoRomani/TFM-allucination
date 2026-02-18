import streamlit as st
import pandas as pd
import time
import asyncio
from pathlib import Path
import json

from src.core.providers.factory import ProviderFactory

# Lazy imports para evitar errores si faltan módulos
try:
    from eval.run_eval import evaluate_row_v0_v1
    from eval.run_eval_v2 import evaluate_row_v2
    from reports.generate_report import generate_report
except ImportError:
    evaluate_row_v0_v1 = None
    evaluate_row_v2 = None
    generate_report = None

def render_tab_reports(provider: str, model_id: str, rag_engine, agent_instance):
    """
    Renderiza la pestaña de Reportes y Evaluación Masiva.
    """
    st.subheader("📊 Centro de Control de Evaluación")
    
    if not evaluate_row_v0_v1:
        st.error("Módulos de evaluación no encontrados. Verifica la carpeta `eval/`.")
        return

    c1, c2 = st.columns([1, 2])
    
    # --- Configuración ---
    with c1:
        st.markdown("### Configuración")
        q_bank_path = st.text_input("Banco de Preguntas", value="eval/question_bank_v1.csv")
        limit_q = st.slider("Límite de Preguntas", 1, 20, 5)
        
        st.markdown("#### Versiones a Evaluar")
        run_v0_v1 = st.checkbox("Ejecutar V0 (Base) y V1 (RAG)", value=True)
        run_v2_eval = st.checkbox("Ejecutar V2 (Agente)", value=True)
        
        st.info(f"Proveedor Activo: **{provider}**\nModelo: **{model_id}**")
        
        if st.button("🚀 Iniciar Benchmark", type="primary"):
            if not Path(q_bank_path).exists():
                st.error("No se encuentra el archivo de preguntas.")
            else:
                st.session_state['run_eval'] = True
    
    # --- Ejecución ---
    with c2:
        st.markdown("### Progreso en Tiempo Real")
        status_container = st.container()
        progress_bar = st.progress(0)
        log_area = st.empty()
        
        if st.session_state.get('run_eval', False):
            st.session_state['run_eval'] = False # Reset trigger
            
            try:
                # 1. Load Data
                df_q = pd.read_csv(q_bank_path, dtype={'id': str})
                if limit_q > 0:
                    df_q = df_q.head(limit_q)
                
                total_steps = len(df_q)
                results_v0_v1 = []
                results_v2 = []
                
                # 2. Prepare Resources
                llm = ProviderFactory.get_provider(provider, model_id)
                rag_chain = rag_engine.get_chain(llm)
                
                # 3. Loop
                for i, row in df_q.iterrows():
                    q_id = row.get('id', str(i))
                    q_text = row.get('question', '')
                    
                    status_container.markdown(f"**Procesando Q{q_id}:** _{q_text}_")
                    
                    # RUN V0/V1
                    if run_v0_v1:
                        log_area.text(f"Evaluando V0/V1 para Q{q_id}...")
                        # Run sync
                        res_1 = evaluate_row_v0_v1(row, llm, rag_chain, provider, model_id, run_label="ui_run")
                        results_v0_v1.append(res_1)
                    
                    # RUN V2
                    if run_v2_eval and agent_instance:
                        log_area.text(f"Evaluando V2 (Agente) para Q{q_id}...")
                        # Run async inside sync streamlit
                        res_2 = asyncio.run(evaluate_row_v2(row, agent_instance))
                        results_v2.append(res_2)
                    
                    progress_bar.progress((i + 1) / total_steps)
                
                st.success("✅ Evaluación Completada")
                
                # 4. Save results
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                
                if results_v0_v1:
                    df_1 = pd.DataFrame(results_v0_v1)
                    # path absolute or relative from project root
                    path_1 = Path(f"eval/results/Comparison/eval_comparison_{provider}_{timestamp}.csv")
                    path_1.parent.mkdir(parents=True, exist_ok=True)
                    df_1.to_csv(path_1, index=False)
                    st.toast(f"Resultados V0/V1 guardados en {path_1.name}")

                if results_v2:
                    path_2 = Path(f"eval/results/V2/eval_v2_{timestamp}.json")
                    path_2.parent.mkdir(parents=True, exist_ok=True)
                    with open(path_2, "w", encoding="utf-8") as f:
                        json.dump(results_v2, f, indent=2, ensure_ascii=False)
                    st.toast(f"Resultados V2 guardados en {path_2.name}")
                
            except Exception as e:
                st.error(f"Error durante evaluación: {e}")

    st.divider()
    
    # --- Generación de Reportes ---
    st.subheader("📄 Generación de Reportes")
    c_rep1, c_rep2 = st.columns(2)
    with c_rep1:
        rep_mode = st.selectbox("Versión del Reporte", ["all", "v0", "v1", "v2"])
        if st.button("Generar Informe Final Markdown"):
            try:
                out_path = generate_report(rep_mode)
                if out_path:
                    st.success(f"Reporte generado: {out_path}")
                    with open(out_path, "rb") as f:
                        st.download_button("⬇️ Descargar Reporte (.md)", f, file_name=Path(out_path).name)
            except Exception as e:
                st.error(f"Error generando reporte: {e}")
