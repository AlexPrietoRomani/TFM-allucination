---
trigger: always_on
---

 1) Propósito del agente

Implementar el proyecto por hitos (H0–H14) y no avanzar si no se cumple el criterio de salida del hito.

Trabajar con el modelo/IDE como plataforma agent-first: el agente puede operar sobre editor + terminal + navegador y se coordina desde una super/ Agent Manager”.

Generar artefactos verificables (diffs, lista de comandos, resultados de tests, evidencia de verificación) en vez de “solo logs”.

2) Seguridad (no negociable)

2.1 Alcance

Solo leer/escribir dentro del workspace del repo. Prohibido tocar rutas externas.

2.2 Prohibición de comandos destructivos por defecto

Prohibido ejecutar: rm -rf, rmdir /s /q, del /s, Remove-Item -Recurse -Force u otros equivalentes.

Excepción: solo si el usuario confirma explícitamente con CONFIRMAR_BORRADO, y el path objetivo se demuestra dentro del repo (mostrar pwd/cd/ls antes).

Justificación: hay reportes recientes de pérdida de datos por agentes que interpretan mal “limpiar cache” y borran rutas equivocadas.

2.3 Autonomía

Operar en modo review-before-execute para terminal/navegador. Evitar modos “turbo/sin confirmación”.

2.4 Secretos

Nunca imprimir ni registrar API keys/tokens.

No commitear .env; configuración con pydantic-settings.

2.5 Descargas desde web

Solo documentos públicos/citables.

Registrar URL + checksum en corpus/registry.yaml.

No descargar contenido con licencia dudosa.

3) Workflow estándar por tarea

3.1 Antes de tocar código

Emitir un Mission Brief (máx. 10 líneas): objetivo, hito, archivos, criterio de salida.

Plan de 3–7 pasos.

Si hay ambigüedad crítica (impacto alto), detener y pedir decisión.

3.2 Implementación

Cambios pequeños y revisables.

Mantener arquitectura modular:

src/core/providers/ (Gemini/OpenRouter + factory)

src/knowledge/ (RAG)

src/metrics/ (métricas)

src/agent/ (LangGraph)

3.3 Verificación mínima obligatoria

Tests (mínimo smoke) deben pasar.

Streamlit arranca (si aplica).

RAG: retrieve() devuelve chunks con metadata completa (doc_id, page, domain).

3.4 Artefactos obligatorios al finalizar

Diff/resumen de cambios.

Comandos ejecutados.

Resultados de tests/ejecución.

Estado del hito: “Done / Blocked / Next”.

4) Reglas específicas del proyecto (anti-errores)

4.1 Proveedores (Gemini/OpenRouter)

Prohibido hardcodear modelos.

Mantener config/model_registry.json sincronizable:

OpenRouter expone listado de modelos vía API.

El selector proveedor/modelo en Streamlit debe leer del registry y fallar temprano con mensaje claro.

4.2 Corpus RAG

Todo documento debe tener doc_id, URL, dominio, checksum, fecha de adquisición.

Chunks trazables: doc_id, page, source_url.

No agregar documentos sin actualizar registry.yaml y versionar.

4.3 Evaluación

Cada corrida: eval/results/{variant}/{timestamp}.parquet + metadata (proveedor, modelo, params, commit).

No cambiar Question Bank sin bump de versión.

4.4 Mitigación (LangGraph / fast-slow path)

El grafo debe ser auditable: registrar scores/decisiones y transiciones.

UX: separar respuesta rápida vs verificación final.

5) Política de comunicación

Cada intervención debe terminar con:

Qué cambió

Cómo se verificó

Qué falta para el hito

Siguiente acción propuesta