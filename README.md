# 🫐 TFM: Mitigación de Alucinaciones en LLMs Agrícolas

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-compose-2496ED.svg)](https://docs.docker.com/compose/)
[![Streamlit](https://img.shields.io/badge/streamlit-app-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Plataforma para el **Trabajo de Fin de Máster** sobre la mitigación y medición de alucinaciones en Modelos de Lenguaje aplicados a la agricultura, con caso de uso en **arándanos y fitosanidad**.

El sistema implementa y compara tres enfoques:

| Versión | Nombre | Descripción |
|---------|--------|-------------|
| **V0** | Baseline | Chat directo con el LLM (sin contexto externo) |
| **V1** | RAG | Retrieval-Augmented Generation con base vectorial |
| **V2** | Agente Autónomo | Sistema con LangGraph, auto-corrección y ciclos de razonamiento |

### Métricas de Calidad

| Métrica | Descripción | Rango |
|---------|-------------|-------|
| **⚖️ Fidelidad** | Mide si la respuesta se deriva exclusivamente del contexto proporcionado, sin inventar datos | 0.0 – 1.0 |
| **🎯 Relevancia** | Mide si los documentos recuperados contienen la información necesaria para responder la pregunta | 0.0 – 1.0 |
| **🔬 FactScore** | Descompone la respuesta en hechos atómicos y verifica cada uno contra el contexto | 0.0 – 1.0 |

---

## 📂 Estructura del Proyecto

```
TFM-allucination/
├── app.py                          # Aplicación principal Streamlit
├── docker-compose.yml              # Stack base (App + Redis + Worker)
├── docker-compose.local.yml        # Override On-Premise (+ Qdrant + Ollama)
├── Dockerfile                      # Imagen de la aplicación
├── pyproject.toml                  # Dependencias (uv)
├── .env.example                    # Variables de entorno (plantilla)
├── ejecution.md                    # Guía completa de ejecución (local/cloud)
│
├── corpus/                         # Corpus de conocimiento
│   ├── registry.yaml               # Registro de metadatos de documentos
│   ├── raw/                        # PDFs y documentos fuente (NO en git)
│   ├── parsed/                     # Markdown pre-procesado con Docling (NO en git)
│   ├── curated_arxiv_ids.json      # IDs curados de ArXiv por batch
│   ├── fetch_phytosanitary_articles.py   # Descarga Batch 1 (IA/DL)
│   └── fetch_phytosanitary_batch2.py     # Descarga Batch 2 (Agronomía)
│
├── src/
│   ├── core/                       # Configuración, proveedores, embeddings
│   │   ├── config/settings.py      # Settings con EXECUTION_MODE (local/cloud)
│   │   └── providers/              # Factory de LLM y Embeddings
│   ├── knowledge/                  # Indexador, cargadores y parsers
│   │   ├── parsers.py              # Docling + TableFlattener + ImageFilter
│   │   ├── loaders.py              # Cargadores polimórficos (PDF/DOCX/XLSX/MD)
│   │   └── indexer.py              # Indexación vectorial (Qdrant)
│   ├── chat/                       # Motor RAG (V1)
│   ├── agent/                      # Agente autónomo LangGraph (V2)
│   └── metrics/                    # Evaluadores (Fidelidad, Relevancia, FactScore)
│
├── scripts/
│   ├── preprocess_corpus.py        # ⭐ Pre-procesamiento de PDFs con Docling
│   ├── build_vector_matrix.py      # 🔬 Construcción masiva de bases vectoriales (Matriz)
│   ├── setup_and_ingest.py         # ⭐ Script de setup automático
│   ├── acquire_corpus.py           # Adquisición manual de corpus
│   └── verify_ingestion.py         # Verificar estado de Qdrant
│
├── eval/                           # Benchmarks y banco de preguntas
│   ├── run_matrix_eval.py          # 🧪 Orquestador de evaluaciones matriciales
│   └── run_eval.py                 # Evaluaciones V0/V1/V2 standard
├── reports/                        # Generación de reportes comparativos
├── services/worker/                # Worker asíncrono (RQ/Redis)
└── docs/                           # Documentación adicional
    ├── PLAN_HITOS_TFM.md           # Plan de hitos detallado del TFM
    └── Documentation.md            # Documentación detallada del TFM
```

---

## 🚀 Guía de Inicio Rápido

El proyecto soporta dos modos de ejecución controlados por la variable `EXECUTION_MODE` en `.env`:

| Modo | Descripción | Requisitos |
|------|-------------|------------|
| `local` | On-Premise, 100% offline | Docker, Ollama |
| `cloud` | APIs en la nube | Google API Key, Qdrant Cloud |
| `híbrido` | Embeddings Locales + Qdrant Cloud | Docker, Ollama, Qdrant Cloud |

> 📖 Para instrucciones detalladas de los modos y configuración Híbrida PRO, consulta [ejecution.md](ejecution.md).

### Prerrequisitos

- **Docker Desktop** (activo y funcionando)
- **Python 3.10+** con [`uv`](https://docs.astral.sh/uv/) instalado
- **Ollama** instalado localmente ([ollama.com](https://ollama.com)) — *solo modo local*

### Paso 1: Clonar y Configurar Variables de Entorno

```bash
git clone https://github.com/TU_USUARIO/TFM-allucination.git
cd TFM-allucination

# Copiar plantilla y editar
cp .env.example .env
# Configurar EXECUTION_MODE=local o EXECUTION_MODE=cloud
```

> **ℹ️ Nota:** En modo `local`, las API keys son opcionales (solo Ollama).
> En modo `cloud`, necesitas `GOOGLE_API_KEY`, `QDRANT_CLOUD_URL` y `QDRANT_CLOUD_API_KEY`.

### Paso 2: Instalar Dependencias Python

```bash
pip install uv    # Si no lo tienes
uv sync           # Instalar dependencias
```

### Paso 3: Levantar Servicios

**Modo Local (On-Premise):**
```bash
docker compose -f docker-compose.yml -f docker-compose.local.yml up -d qdrant redis ollama
```

**Modo Cloud:**
```bash
docker compose up -d redis
```

### Paso 4: Descargar Modelos Ollama *(solo modo local)*

```bash
ollama pull qwen2.5:3b
ollama pull qwen3-embedding
```

| Modelo | Uso | Tamaño |
|--------|-----|--------|
| `qwen2.5:3b` | LLM para chat/métricas | 1.9 GB |
| `qwen3-embedding` | Embeddings (por defecto) | 4.7 GB |

### Paso 5: Obtener Documentos del Corpus

```bash
uv run corpus/fetch_phytosanitary_articles.py
uv run corpus/fetch_phytosanitary_batch2.py
```

### Paso 5.5: Pre-procesar PDFs *(opcional pero recomendado)*

```bash
# Convierte PDFs tabulares a Markdown estructurado con Docling
uv run scripts/preprocess_corpus.py --skip-images
```

Esto genera archivos `.md` en `corpus/parsed/` que preservan tablas y metadata.
El indexador prioriza estos archivos sobre los PDFs crudos.

### Paso 6: Setup Automático (Indexación + Verificación)

```bash
uv run scripts/setup_and_ingest.py
```

Este script indexa los documentos en la colección Qdrant correspondiente al proveedor de embeddings:
- `tfm_allucination_ollama` (Embeddings locales, modo local/híbrido)
- `tfm_allucination_gemini` (Embeddings Gemini 3072d, modo cloud)

### Paso 7: Iniciar la Aplicación

```bash
uv run streamlit run app.py
```

👉 Abrir **http://localhost:8501**

---

## 🖥️ Uso de la Aplicación

### Pestañas Principales

| Pestaña | Función |
|---------|---------|
| ⚔️ **Comparativa** | Compara V0 vs V1, V1 vs V2, V0 vs V2, o **V0 vs V1 vs V2** (triple) |
| 🧠 **V0 (Baseline)** | Chat directo con el LLM sin contexto |
| 📚 **V1 (RAG)** | Chat con documentos + métricas de calidad |
| 🤖 **V2 (Agente)** | Agente autónomo con pasos de razonamiento + métricas |
| 📊 **Matriz de Experimentos** | Tablero visual con Boxplots, Pareto y Desglose de Latencia interactivo |
| 📊 **Reportes** | Benchmarks automáticos y generación de informes |

### Métricas en la UI

Cuando activas **"📊 Calcular Métricas"** en la barra lateral, cada respuesta de V1 y V2 se evalúa con:

- **⚖️ Fidelidad (Faithfulness):** LLM-as-a-Judge evalúa si cada afirmación de la respuesta está soportada por el contexto. Score 1.0 = cero alucinaciones.
- **🎯 Relevancia (Context Relevance):** Evalúa si los documentos recuperados contienen la información necesaria. Score 1.0 = contexto perfecto.
- **🔬 FactScore:** Descompone la respuesta en hechos atómicos individuales y verifica cada uno contra el contexto. Muestra desglose: ✅ Soportado / ❌ Contradicho / ⚠️ No verificado.

> **Nota:** Las métricas usan Ollama (`qwen2.5:3b`) como juez evaluador. Es más lento pero funciona 100% offline y sin cuota de API.

---

## 🐋 Despliegue Completo con Docker

### Modo Local (On-Premise)

```bash
# 1. Configurar .env (EXECUTION_MODE=local)
cp .env.example .env

# 2. Levantar todo el stack local
docker compose -f docker-compose.yml -f docker-compose.local.yml up -d --build

# 3. Descargar modelos en Ollama (dentro del contenedor)
docker exec -it tfm-ollama ollama pull qwen2.5:3b
docker exec -it tfm-ollama ollama pull mxbai-embed-large

# 4. Indexar documentos
docker exec -it tfm-app uv run scripts/setup_and_ingest.py --skip-ollama

# 5. Abrir http://localhost:8501
```

### Modo Cloud Completo

```bash
# 1. Configurar .env (EXECUTION_MODE=cloud, API keys, Qdrant Cloud URL, DEFAULT_EMBEDDING_PROVIDER=gemini o ollama)
cp .env.example .env

# 2. Levantar app + redis (y ollama si usas proveedor híbrido)
# Modificar docker-compose según ejecution.md
docker compose up -d --build

# 3. Indexar documentos (hacia Qdrant Cloud)
docker exec -it tfm-app uv run scripts/setup_and_ingest.py --skip-ollama

# 4. Abrir http://localhost:8501
```

### Modelos Ollama Recomendados

| Modelo | Tamaño | Uso | Recomendación |
|--------|--------|-----|---------------|
| `qwen2.5:3b` | 1.9 GB | LLM Chat/Métricas | ⭐ **Recomendado** |
| `nomic-embed-text` | 274 MB | Embeddings (768d) | ⭐ Ligero/Rápido |
| `mxbai-embed-large` | 670 MB | Embeddings SOTA | 🚀 **Recomendado (Alta Precisión)** |
| `snowflake-arctic-embed:latest` | 335 MB | Multilingüe | Alternativa |
| `qwen2.5:3b` | 1.8 GB | Mini LLM (Default) | ✅ Balanceado |
| `qwen2.5:7b` | 4.7 GB | LLM más potente | Si tienes +8GB RAM |
| `phi3:mini` | 2.3 GB | Razonamiento | Alternativa |
| `llama3.2:latest` | 2.0 GB | LLM Chat texto | Alternativa |

---

## 📚 Gestión del Corpus de Conocimiento

### Agregar Documentos Manualmente

```bash
# 1. Copiar archivo
cp mi_articulo.pdf corpus/raw/mi-articulo-id.pdf

# 2. Agregar entrada en corpus/registry.yaml
# 3. Re-indexar
uv run scripts/setup_and_ingest.py
```

### Formato de `registry.yaml`

```yaml
documents:
  - id: mi-articulo-id
    title: "Título del documento"
    url: "https://..."
    type: pdf
    language: es
    tags: [fitosanidad, arándanos]
    description: "Descripción breve..."
    year: 2024
    country: Chile
    source: "Revista XYZ"
    doc_type: "Artículo científico"
```

---

## 📊 Evaluación y Benchmarks

```bash
# Evaluación V0 y V1
uv run eval/run_eval.py

# Evaluación V2 (Agente)
uv run eval/run_eval_v2.py

# Métricas V1 (Faithfulness / FactScore)
uv run eval/run_metrics.py
uv run eval/run_factscore.py

# Generar reporte 
uv run reports/generate_report.py --mode all
```

---

## 🔧 Troubleshooting

| Problema | Solución |
|----------|----------|
| Qdrant no responde | `docker compose restart qdrant` |
| Ollama sin modelo | `ollama pull qwen2.5:3b && ollama pull mxbai-embed-large` |
| Métricas no aparecen | Activar checkbox "📊 Calcular Métricas" en la barra lateral |
| FactScore vacío | Verificar que Ollama esté activo y el modelo descargado |
| Re-indexar | `uv run scripts/setup_and_ingest.py --force-reindex` |
| Error de embeddings | Verificar que `mxbai-embed-large` esté descargado en Ollama |

---

## 📄 Documentación Adicional

- [Guía de Ejecución (Local / Cloud)](ejecution.md)
- [Documentación Detallada del TFM](docs/Documentation.md)
- [Plan de Hitos del TFM](docs/PLAN_HITOS_TFM.md)
- [Arquitectura y Comparativa Técnica](docs/ARQUITECTURA_Y_COMPARATIVA.md)
- [Protocolo Experimental](docs/protocolo_experimental.md)
- [Definición Matemática de Métricas](docs/METRICAS_IMPLEMENTADAS.md)

---

## 📝 Licencia

Este proyecto es parte de un Trabajo de Fin de Máster académico.
