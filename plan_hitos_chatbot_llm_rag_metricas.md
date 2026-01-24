# Plan por Hitos — Chatbot LLM (Python + Streamlit) con RAG, Métricas y Mitigación

Este documento consolida el plan por hitos para construir un chatbot con:

- **Backend en Python** (servicios modulares).
- **Frontend en Streamlit** (chat UI).
- **LangChain desde el inicio**.
- Proveedores **Gemini** y **OpenRouter** integrados de forma robusta (validación anti-errores).
- **RAG** con un corpus agronómico seleccionado para maximizar diferencia vs “chat normal”.
- **Métricas** (incertidumbre / riesgo de alucinación y factualidad) y **mitigación activa** con orquestación (LangGraph).
- **Hito explícito** de búsqueda/descarga/curación de PDFs/tablas para el RAG.

> Nota: El plan mantiene la estructura y contenido previamente definidos. Se agregan únicamente precisiones operativas (convenciones, estructura de repositorio, gates y herramientas auxiliares).

---

## 1) Stack objetivo (constante en el plan)

### Frontend
- **Streamlit**: UI conversacional con `st.chat_message` y `st.chat_input`.

### Backend / Core
- **LangChain** (LCEL/Runnables) para pipelines desde el inicio.
- **LangGraph** para orquestación agéntica/estado (Self‑RAG/CRAG style) en hitos avanzados.
- **Vector DB**: **Qdrant** vía `langchain-qdrant`.
- **PDF ingestion**: `PyPDFLoader` y/o `UnstructuredPDFLoader`.

### Proveedores LLM (desde Hito 1)
- **Gemini (Google)**: `langchain-google-genai` (`ChatGoogleGenerativeAI`) con `GOOGLE_API_KEY`.
- **OpenRouter**: endpoint **OpenAI-compatible** (`https://openrouter.ai/api/v1`) vía `ChatOpenAI` + `OPENROUTER_API_KEY`; headers opcionales `HTTP-Referer` y `X-Title`.

---

## 2) Convenciones operativas (recomendadas)

### 2.1 Gestión de configuración
- Archivo `.env` (no versionado) + `.env.example` (versionado).
- Validación de variables con `pydantic-settings`.
- Variables mínimas:
  - `GOOGLE_API_KEY`
  - `OPENROUTER_API_KEY`
  - `OPENROUTER_HTTP_REFERER` (opcional)
  - `OPENROUTER_X_TITLE` (opcional)
  - `QDRANT_URL` (p. ej. `http://localhost:6333`)
  - `QDRANT_API_KEY` (si aplica)

### 2.2 Estructura de repositorio (mínima y escalable)

Sugerida (puede ajustarse sin romper el plan):

- `app.py` (Streamlit)
- `src/`
  - `core/`
    - `config/` (settings/env)
    - `providers/` (Gemini/OpenRouter + factory)
    - `logging/` (trace_id, jsonl)
  - `chat/` (chains V0/V1)
  - `knowledge/` (loaders, splitters, indexer, retriever)
  - `metrics/` (semantic entropy, factscore)
  - `agent/` (LangGraph)
- `corpus/`
  - `registry.yaml` (metadata)
  - `raw/` (PDFs)
  - `processed/` (texto/chunks opcional)
- `eval/`
  - `question_bank_v1.csv`
  - `results/` (V0/V1/V2)
- `scripts/`
  - `sync_model_registry.py`
  - `acquire_corpus.py`
- `reports/` (markdown/quarto)
- `tests/` (smoke + integración)
- `docker-compose.yml` (Qdrant/Redis/worker según hito)

### 2.3 Versionado y reproducibilidad
- Recomendado fijar versiones en `pyproject.toml` (Poetry/uv) o `requirements.txt`.
- Registrar en cada corrida (eval/run):
  - proveedor, modelo, parámetros, hash del corpus, hash del código (commit) y timestamp.

### 2.4 Gate de avance por hito
- Cada hito tiene **Criterio de salida** y **Entregables** obligatorios.
- Si un criterio no se cumple, se corrige antes de avanzar.

---

## 3) Tema recomendado para maximizar alucinación y “delta” con RAG

**Tema**: Manejo fitosanitario en arándano orientado a cumplimiento de etiqueta.

**Subtema específico**:
- **REI/PHI**, selección de activos por **grupo FRAC** (resistencia) y restricciones por **MRL** para exportación.

**Motivación**: alta propensión a alucinación por dependencia de números/reglas/etiquetas que cambian y por necesidad de evidencia.

---

## 4) Corpus RAG — búsqueda, descarga y curación (insumos)

El corpus debe incluir (mínimo viable):

- Documentos normativos y definiciones (REI/WPS, etiquetas, definiciones de PHI).
- Tablas oficiales (FRAC code list).
- Guías IPM/arándano (extensión universitaria).
- Documentos/tablas de MRL (por mercado o referencia estándar).

Se administran mediante `corpus/registry.yaml` con checksum.

---

# 5) Plan por hitos (detallado)

## Hito 0 — Protocolo experimental y criterios de éxito (TFM-ready)

**Meta**: Definir qué comparas y cómo lo mides (V0/V1/V2) antes de construir.

**Tecnologías**: Python (pandas), Markdown, repo `docs/`.

**Tareas**
1. Definir variantes:
   - **V0**: Chat “normal” (sin RAG, sin métricas).
   - **V1**: Chat con RAG y citas.
   - **V2**: RAG + mitigación (gating por incertidumbre + verificación factual).
2. Crear **Question Bank** (30–60 preguntas) del tema elegido.
3. Definir **ground truth** por pregunta.
4. Definir métricas:
   - Factualidad (FactScore-style).
   - Incertidumbre/riesgo (Semantic Entropy-style).
   - Operativas: TTFT, latencia total, #calls LLM, costo (si disponible).

**Criterio de salida**
- `docs/protocolo_experimental.md` con V0/V1/V2 + reglas.
- `eval/question_bank_v1.csv` (o JSON) versionado.

**Entregables**
- Protocolo + dataset de evaluación inicial.

---

## Hito 1 — Proyecto base + configuración de proveedores (sin UI todavía)

**Meta**: Core LangChain que invoca **Gemini y OpenRouter** sin errores, con validación básica de credenciales.

**Tecnologías / librerías**
- `langchain`, `langchain-openai`, `langchain-google-genai`
- `python-dotenv`, `pydantic-settings`
- `pytest` (smoke tests)

**Tareas**
1. Estructura repo mínima:
   - `src/core/config/`
   - `src/core/providers/`
   - `tests/test_providers_smoke.py`
2. **Gemini**: configurar `GOOGLE_API_KEY` y wrapper.
3. **OpenRouter**: `OPENROUTER_API_KEY`, `base_url=https://openrouter.ai/api/v1`, headers opcionales.

**Criterio de salida**
- Tests pasan:
  - `gemini.invoke("ping")` responde.
  - `openrouter.invoke("ping")` responde.
- Logs con proveedor/modelo/latencia/trace_id.

**Entregables**
- `src/core/providers/{gemini.py, openrouter.py, factory.py}`
- `.env.example` documentado.

---

## Hito 2 — Registro de modelos y validación anti-errores (model registry)

**Meta**: Evitar errores de “modelo no existe”/nombres incorrectos.

**Tecnologías / librerías**
- HTTP client (requests/httpx)
- Sync scripts en `scripts/`

**Tareas**
1. `scripts/sync_model_registry.py`:
   - OpenRouter: `GET /models` → guarda JSON.
   - Gemini: listar/validar modelos vía API/SDK → guarda metadata.
2. Persistir `config/model_registry.json`:
   - `provider`, `model_id`, `context_length`, `pricing` (si aplica), `updated_at`.
3. `ProviderFactory` valida `model_id` contra registry.

**Criterio de salida**
- Sync genera registry.
- Modelo inválido falla temprano con error claro.

**Entregables**
- `config/model_registry.json`
- `scripts/sync_model_registry.py`

---

## Hito 3 — Chat baseline V0 en Streamlit (LangChain desde el día 1)

**Meta**: UI de chat funcional con memoria mínima, usando LangChain directo a LLM.

**Tecnologías / librerías**
- Streamlit chat UI
- Factory de modelos (H1/H2)

**Tareas**
1. `app.py`:
   - `st.session_state` (historial)
   - selector proveedor/modelo (desde registry)
2. Pipeline LangChain:
   - PromptTemplate + `ChatModel` + parser.
3. Logging local `runs/trace.jsonl`.

**Criterio de salida**
- Chat funciona con ambos proveedores.
- Historial operativo (ventana corta).

**Entregables**
- `app.py` + `src/core/chat_baseline.py`
- `docs/operacion_chat_v0.md`

---

## Hito 4 — Harness de evaluación automática (V0)

**Meta**: Ejecutar Question Bank contra V0 y guardar outputs comparables.

**Tecnologías**
- pandas, json, tqdm

**Tareas**
1. `eval/run_eval.py --variant V0 --provider ... --model ...`
2. Persistir `eval/results/V0/{timestamp}.parquet`:
   - `question_id`, `prompt`, `response`, `model`, `latency`, `tokens` (si aplica)
3. Parámetros controlados (temperatura baja, etc.).

**Criterio de salida**
- Ejecuta 30–60 preguntas sin fallar.
- Resultados persistidos/versionados.

**Entregables**
- `eval/run_eval.py`
- `eval/results/V0/...`

---

## Hito 5 — Búsqueda, descarga y curación del corpus RAG (PDFs/tablas)

**Meta**: Corpus RAG formal, trazable y versionado.

**Tecnologías / librerías**
- `scripts/acquire_corpus.py` (requests)
- `corpus/registry.yaml`

**Tareas**
1. Definir lista de fuentes y URLs.
2. Crear `corpus/registry.yaml`:
   - `doc_id`, título, editorial, año, url, dominio, licencia/nota, checksum.
3. `scripts/acquire_corpus.py`:
   - descarga + verificación checksum → `corpus/raw/`.
4. QA manual: verificar que contengan “hechos consultables”.

**Criterio de salida**
- ≥10 documentos relevantes descargados y registrados.
- Cada documento con metadata + checksum.

**Entregables**
- `corpus/registry.yaml`
- `corpus/raw/*.pdf`
- `scripts/acquire_corpus.py`

---

## Hito 6 — Ingestión PDF → Document objects (LangChain loaders)

**Meta**: Transformar PDFs a `Document` con metadata consistente.

**Tecnologías / librerías**
- `PyPDFLoader` (rápido), fallback `UnstructuredPDFLoader`.
- `langchain-text-splitters`

**Tareas**
1. Loader unificado: `load_pdf(doc_path) -> List[Document]`.
2. Normalizar metadata: `doc_id`, `source`, `page`, `section`, `published_year`, `domain`.
3. QA de extracción (texto vacío/encoding) y fallback.

**Criterio de salida**
- 90%+ PDFs extraen texto utilizable.
- Trazabilidad a doc + página.

**Entregables**
- `src/knowledge/loaders.py`
- `reports/ingestion_qa.md`

---

## Hito 7 — Vectorización y almacenamiento en Qdrant

**Meta**: Construir índice vectorial consultable por dominio.

**Tecnologías / librerías**
- Qdrant + `langchain-qdrant`
- `docker-compose.yml` (Qdrant local)

**Tareas**
1. Definir colecciones o payload `domain`.
2. Indexación (upsert) de chunks.
3. Tests de recuperación (REI/FRAC).

**Criterio de salida**
- `retrieve(query)` devuelve top‑k chunks con metadata correcta.
- Persistencia estable tras reinicio.

**Entregables**
- `docker-compose.yml` (Qdrant)
- `src/knowledge/indexer.py`

---

## Hito 8 — Chat RAG V1 (con citas y política “no inventar”)

**Meta**: Chat con RAG + citas visibles en Streamlit.

**Tecnologías**
- LangChain retrieval chain
- Streamlit para render de citas

**Tareas**
1. Chain: `retrieve -> synthesize -> answer_with_citations`.
2. Política: si no hay evidencia, abstenerse y declarar falta de soporte.
3. UI: panel “Sources” + evidencia expandible.

**Criterio de salida**
- Preguntas con números/reglas: siempre cita o abstiene.
- V1 corre el Question Bank completo.

**Entregables**
- `src/chat/rag_chain.py`
- `eval/results/V1/...`

---

## Hito 9 — Evaluación comparativa V0 vs V1 (primer “delta”)

**Meta**: Cuantificar mejora por introducir RAG.

**Tecnologías**
- pandas + reporte (Markdown/Notebook)

**Tareas**
1. Ejecutar eval V0 y V1.
2. Reportar:
   - tasa de “sin cita” donde se exige soporte
   - error manual (subset) o heurística.

**Criterio de salida**
- Evidencia clara de mejora V1 > V0.

**Entregables**
- `reports/v0_vs_v1.md` + tablas

---

## Hito 10 — Métrica 1: Riesgo de alucinación por muestreo (Semantic Entropy style)

**Meta**: Estimar incertidumbre mediante múltiples generaciones y agrupación semántica.

**Tecnologías**
- LangChain multi-sampling
- Persistencia de runs

**Tareas**
1. `uncertainty_service`:
   - N muestras (temperatura > 0)
   - clustering semántico
   - score final
2. Persistir muestras, clusters, score.

**Criterio de salida**
- Score estable y correlacionable con errores (al menos en subset).

**Entregables**
- `src/metrics/semantic_entropy.py`
- `eval/results/uncertainty/...`

---

## Hito 11 — Métrica 2: FactScore-style (hechos atómicos + verificación con evidencia)

**Meta**: Medir factualidad por afirmaciones verificables.

**Tecnologías**
- LangChain extraction + judge
- Reuso de evidencias del retriever

**Tareas**
1. Extractor de claims atómicos.
2. Verificador claim vs evidencia.
3. FactScore: % supported y reporte de fallos.

**Criterio de salida**
- Diagnóstico por claim (qué falló y por qué).

**Entregables**
- `src/metrics/factscore.py`
- `reports/factscore_examples.md`

---

## Hito 12 — Orquestación con LangGraph (V2: mitigación activa)

**Meta**: Reducir alucinación automáticamente (no solo medir).

**Tecnologías**
- LangGraph (StateGraph)

**Tareas**
1. Definir grafo:
   - `classify -> retrieve -> draft -> eval(SE, FactScore) -> decide -> revise/abstain`.
2. Políticas:
   - SE alta → más retrieval / reescritura “solo evidencia”.
   - FactScore bajo → abstenerse o pedir dato faltante.
3. UI modo “Explain”: mostrar estados y decisiones.

**Criterio de salida**
- V2 end-to-end con trazabilidad por nodo.

**Entregables**
- `src/agent/graph.py`
- `docs/graph_policy.md`

---

## Hito 13 — Asincronía (fast/slow path) + experiencia de usuario

**Meta**: Mantener chat ágil aunque FactScore sea costoso.

**Tecnologías**
- Celery/RQ + Redis (patrón enterprise)
- Streamlit status

**Tareas**
1. Respuesta rápida con draft.
2. Verificación lenta en worker.
3. UI: badges de estado.

**Criterio de salida**
- TTFT bajo; verificación llega después sin romper conversación.

**Entregables**
- `services/worker/`
- `docker-compose.yml` (Redis + worker)

---

## Hito 14 — Evaluación final V0/V1/V2 + paquete del “PDF de Métricas”

**Meta**: Resultados y material del TFM reproducible.

**Tecnologías**
- pipeline de evaluación
- reporte final en Markdown/Quarto/LaTeX

**Tareas**
1. Ejecutar evaluación completa.
2. Reportar:
   - distribuciones SE/FactScore
   - comparativos V0/V1/V2
   - latencia/costo/#calls
3. Anexos:
   - prompts, registry de documentos, versionado de modelos.

**Criterio de salida**
- Documento final reproducible y defendible.

**Entregables**
- `reports/final_metrics.pdf` (o fuente)
- `eval/results/final/` + `corpus/registry.yaml` + `config/model_registry.json`

---

## 6) Reglas prácticas para no tener errores con proveedores (desde el día 1)

1. **Nunca hardcodear modelos**: sincroniza y valida contra `model_registry.json`.
2. **Variables de entorno canónicas**:
   - Gemini: `GOOGLE_API_KEY`.
   - OpenRouter: `OPENROUTER_API_KEY` + `base_url` OpenAI-compatible.
3. **Headers OpenRouter** (recomendado): `HTTP-Referer`, `X-Title`.
4. **Logs obligatorios** por request: `trace_id`, proveedor, modelo, parámetros, latencia.

---

## 7) Checklist rápido de gates (resumen ejecutivo)

- **H0**: Protocolo + Question Bank + ground truth.
- **H1**: Proveedores funcionando con tests.
- **H2**: Registry y validación anti-errores.
- **H3**: Streamlit chat V0 operativo.
- **H4**: Harness V0 produce resultados.
- **H5–H7**: Corpus descargado, cargado y vectorizado.
- **H8**: RAG V1 con citas y abstención si no hay evidencia.
- **H9**: Reporte V0 vs V1.
- **H10–H11**: Métricas implementadas y persistidas.
- **H12–H13**: Mitigación y asincronía integradas.
- **H14**: Evaluación final + PDF de métricas.
