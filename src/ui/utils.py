import streamlit as st
import time
import asyncio
from typing import Dict, List, Any
from langchain_core.documents import Document

# Import Metrics (Lazy load to handle missing deps gracefully in UI)
try:
    from src.metrics.faithfulness import FaithfulnessMetric
    from src.metrics.context_relevance import ContextRelevanceMetric
    from src.metrics.factscore import FactScoreMetric
except ImportError:
    FaithfulnessMetric = None
    ContextRelevanceMetric = None
    FactScoreMetric = None

def render_metrics(metrics_data: Dict[str, Any]):
    """
    Renderiza las métricas de calidad con descripciones detalladas en la UI de Streamlit.
    """
    if not metrics_data:
        return
    
    with st.expander("📊 Métricas de Calidad", expanded=True):
        mc1, mc2, mc3 = st.columns(3)
        
        faith_score = metrics_data.get('faith_score', 0.0)
        rel_score = metrics_data.get('rel_score', 0.0)
        fs_score = metrics_data.get('factscore', 0.0)
        
        with mc1:
            st.metric("⚖️ Fidelidad", f"{faith_score:.2f}")
            st.caption("_Mide si la respuesta se deriva exclusivamente del contexto, sin inventar datos._")
        with mc2:
            st.metric("🎯 Relevancia", f"{rel_score:.2f}")
            st.caption("_Mide si los documentos recuperados contienen la información necesaria._")
        with mc3:
            st.metric("🔬 FactScore", f"{fs_score:.2f}")
            st.caption("_Descompone la respuesta en hechos atómicos y verifica cada uno._")
        
        # Razones detalladas
        faith_reason = metrics_data.get('faith_reason', '')
        rel_reason = metrics_data.get('rel_reason', '')
        
        if faith_reason:
            st.info(f"**Fidelidad:** {faith_reason}")
        if rel_reason:
            st.info(f"**Relevancia:** {rel_reason}")
        
        # Desglose FactScore
        if "fs_breakdown" in metrics_data and metrics_data["fs_breakdown"]:
            st.markdown("---")
            supported = metrics_data.get('supported_claims', 0)
            total = metrics_data.get('total_claims', 0)
            st.markdown(f"**Desglose FactScore** ({supported}/{total} soportados)")
            
            for item in metrics_data["fs_breakdown"]:
                label = item.get('label', 'NoVerificado')
                claim = item.get('claim', '')
                reason = item.get('reason', '')
                
                if label == 'Soportado':
                    st.markdown(f"✅ {claim}")
                elif label == 'Contradicho':
                    st.markdown(f"❌ {claim} — _{reason}_")
                else:
                    st.markdown(f"⚠️ {claim} — _{reason}_")

def normalize_docs(docs: List[Any]) -> List[Document]:
    """
    Asegura que la lista de documentos sean objetos Document de LangChain.
    Si son dicts, los convierte.
    """
    normalized = []
    for d in docs:
        if isinstance(d, Document):
            normalized.append(d)
        elif isinstance(d, dict):
            # Recrear Document desde dict
            content = d.get("page_content", "")
            meta = d.get("metadata", {})
            normalized.append(Document(page_content=content, metadata=meta))
        else:
            # Fallback string
            normalized.append(Document(page_content=str(d), metadata={}))
    return normalized

def calculate_metrics_sync(prompt: str, response: str, retrieved_docs: List[Any], use_metrics: bool, status_container=None, provider=None, model_id=None) -> Dict[str, Any]:
    """
    Calcula las métricas (Fidelidad, Relevancia, FactScore) de forma síncrona.
    Retorna un diccionario con los scores y razones.
    """
    metrics = {}
    
    # Si no se solicitan métricas o no están disponibles las clases, retornar vacío
    if not use_metrics or FaithfulnessMetric is None:
        return metrics
    
    # Normalizar docs para asegurar que tienen .page_content y .metadata
    docs_objects = normalize_docs(retrieved_docs)
    
    try:
        # 1. Fidelidad
        if status_container:
            status_container.write("⚖️ Calculando Fidelidad...")
        
        faith_metric = FaithfulnessMetric(provider=provider, model_id=model_id)
        faith_res = faith_metric.evaluate(response, docs_objects)
        
        # 2. Relevancia
        if status_container:
            status_container.write("🎯 Calculando Relevancia...")
            
        rel_metric = ContextRelevanceMetric(provider=provider, model_id=model_id)
        rel_res = rel_metric.evaluate(prompt, docs_objects)
        
        metrics.update({
            "faith_score": faith_res.get("score", 0.0),
            "faith_reason": faith_res.get("reason", "N/A"),
            "rel_score": rel_res.get("score", 0.0),
            "rel_reason": rel_res.get("reason", "N/A"),
        })
        
        # 3. FactScore 
        # (Solo si hay documentos recuperados y FactScoreMetric está disponible)
        if FactScoreMetric and docs_objects:
            if status_container:
                status_container.write("🔬 Calculando FactScore (puede tardar)...")
            
            try:
                fs_metric = FactScoreMetric(provider=provider, model_id=model_id)
                fs_res = fs_metric.calculate(response, docs_objects)
                
                metrics.update({
                    "factscore": fs_res.get("score", 0.0),
                    "total_claims": fs_res.get("total_claims", 0),
                    "supported_claims": fs_res.get("supported_claims", 0),
                    "fs_breakdown": fs_res.get("breakdown", [])
                })
            except Exception as e:
                print(f"Error FactScore: {e}")
                metrics["factscore"] = 0.0
                metrics["fs_breakdown"] = []
                
    except Exception as e:
        if status_container:
            status_container.error(f"Error al calcular métricas: {e}")
        else:
            print(f"Error métricas: {e}")
            
    return metrics

async def run_agent_v2(agent_instance, prompt: str, status_box=None):
    """
    Ejecuta el agente V2 (LangGraph) y captura tanto la respuesta final como los documentos recuperados
    durante el proceso (si el grafo emite eventos de recuperación).
    """
    log = []
    final_resp = ""
    docs = []
    
    # Usamos astream_events para capturar eventos internos del grafo
    # Específicamente buscamos el output del nodo 'retrieve'
    async for event in agent_instance.app.astream_events({"question": prompt}, version="v1"):
        kind = event["event"]
        name = event["name"]
        
        # Logging visual en el status box
        if status_box and kind == "on_chain_start" and name in ["retrieve", "generate", "grade", "classify", "chitchat"]:
            status_box.write(f"▶️ V2 Nodo: **{name}**")
            log.append(f"Start: {name}")
            
        # Captura de documentos del retriever
        # Ajustamos para interceptar correctamente la salida del retriever en V2
        if kind == "on_chain_end" and name == "retrieve":
             data = event["data"].get("output")
             if data:
                 if isinstance(data, dict) and "documents" in data:
                     docs = data["documents"]
                 elif hasattr(data, "documents"): # Por si es un objeto state
                     docs = data.documents
                 elif isinstance(data, list): # Si el retriever retorna lista directa
                     docs = data

    # Ejecución final para obtener la respuesta
    final_state = await agent_instance.app.ainvoke({"question": prompt})
    final_resp = final_state.get("generation", "")
    
    # Fallback: Si no capturamos docs por eventos, intentamos sacarlos del estado final
    if not docs and "documents" in final_state:
        docs = final_state["documents"]
        
    return final_resp, docs, log
