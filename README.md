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
├── docker-compose.yml              # Stack completo (Qdrant + Redis + Ollama + App)
├── Dockerfile                      # Imagen de la aplicación
├── pyproject.toml                  # Dependencias (uv)
├── .env.example                    # Variables de entorno (plantilla)
├── PLAN_HITOS_TFM.md               # Plan de hitos detallado del TFM
│
├── corpus/                         # Corpus de conocimiento
│   ├── registry.yaml               # Registro de metadatos de documentos
│   ├── raw/                        # PDFs y documentos fuente (NO en git)
│   ├── curated_arxiv_ids.json      # IDs curados de ArXiv por batch
│   ├── fetch_phytosanitary_articles.py   # Descarga Batch 1 (IA/DL)
│   └── fetch_phytosanitary_batch2.py     # Descarga Batch 2 (Agronomía)
│
├── src/
│   ├── core/                       # Configuración, proveedores, embeddings
│   │   └── providers/embeddings.py # EmbeddingFactory (Ollama nomic-embed-text)
│   ├── knowledge/                  # Indexador y cargadores de documentos
│   ├── chat/                       # Motor RAG (V1)
│   ├── agent/                      # Agente autónomo LangGraph (V2)
│   └── metrics/                    # Evaluadores (Fidelidad, Relevancia, FactScore)
│       ├── faithfulness.py         # Métrica de Fidelidad (LLM-as-a-Judge)
│       ├── context_relevance.py    # Métrica de Relevancia del Contexto
│       ├── factscore.py            # FactScore (extracción + verificación atómica)
│       └── judges.py               # Factory del LLM juez (Ollama local)
│
├── scripts/
│   ├── setup_and_ingest.py         # ⭐ Script de setup automático
│   ├── acquire_corpus.py           # Adquisición manual de corpus
│   └── verify_ingestion.py         # Verificar estado de Qdrant
│
├── eval/                           # Benchmarks y banco de preguntas
├── reports/                        # Generación de reportes comparativos
├── services/worker/                # Worker asíncrono (RQ/Redis)
└── docs/                           # Documentación adicional
```

---

## 🚀 Guía de Inicio Rápido

### Prerrequisitos

- **Docker Desktop** (activo y funcionando)
- **Python 3.10+** con [`uv`](https://docs.astral.sh/uv/) instalado
- **Ollama** instalado localmente ([ollama.com](https://ollama.com))

### Paso 1: Clonar y Configurar Variables de Entorno

```bash
git clone https://github.com/TU_USUARIO/TFM-allucination.git
cd TFM-allucination

# Copiar plantilla y editar con tus API keys
cp .env.example .env
# Editar .env con tu editor favorito
```

> **ℹ️ Nota:** Si solo usas Ollama (100% local), las API keys son opcionales.  
> Si quieres usar Gemini/OpenRouter, necesitas `GOOGLE_API_KEY` y/o `OPENROUTER_API_KEY`.

### Paso 2: Instalar Dependencias Python

```bash
pip install uv    # Si no lo tienes
uv sync           # Instalar dependencias
```

### Paso 3: Levantar Qdrant y Redis (Docker)

```bash
docker compose up -d qdrant redis
```

### Paso 4: Descargar los Modelos Ollama

```bash
# Modelo LLM (chat e inferencia)
ollama pull qwen2.5:3b

# Modelo de Embeddings (indexación y búsqueda vectorial)
ollama pull nomic-embed-text
```

| Modelo | Uso | Tamaño |
|--------|-----|--------|
| `qwen2.5:3b` | LLM para chat/métricas | 1.9 GB |
| `nomic-embed-text` | Embeddings vectoriales | 274 MB |

### Paso 5: Obtener Documentos del Corpus

```bash
# Batch 1: 30 artículos de detección de plagas/enfermedades con IA
uv run corpus/fetch_phytosanitary_articles.py

# Batch 2: 30 artículos de agronomía de campo
uv run corpus/fetch_phytosanitary_batch2.py
```

### Paso 6: Setup Automático (Indexación + Verificación)

```bash
uv run scripts/setup_and_ingest.py
```

Este script:
1. ✅ Verifica que Qdrant y Ollama estén activos
2. ✅ Verifica que `qwen2.5:3b` y `nomic-embed-text` estén descargados
3. ✅ Indexa todos los documentos en Qdrant usando embeddings de Ollama (768d)

**Opciones:**
```bash
uv run scripts/setup_and_ingest.py --skip-ollama      # Sin verificar Ollama
uv run scripts/setup_and_ingest.py --model qwen2.5:7b  # Modelo diferente
uv run scripts/setup_and_ingest.py --force-reindex     # Re-indexar todo
```

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
| 📊 **Reportes** | Benchmarks automáticos y generación de informes |

### Métricas en la UI

Cuando activas **"📊 Calcular Métricas"** en la barra lateral, cada respuesta de V1 y V2 se evalúa con:

- **⚖️ Fidelidad (Faithfulness):** LLM-as-a-Judge evalúa si cada afirmación de la respuesta está soportada por el contexto. Score 1.0 = cero alucinaciones.
- **🎯 Relevancia (Context Relevance):** Evalúa si los documentos recuperados contienen la información necesaria. Score 1.0 = contexto perfecto.
- **🔬 FactScore:** Descompone la respuesta en hechos atómicos individuales y verifica cada uno contra el contexto. Muestra desglose: ✅ Soportado / ❌ Contradicho / ⚠️ No verificado.

> **Nota:** Las métricas usan Ollama (`qwen2.5:3b`) como juez evaluador. Es más lento pero funciona 100% offline y sin cuota de API.

---

## 🐋 Despliegue Completo con Docker

```bash
# 1. Configurar .env
cp .env.example .env

# 2. Levantar todo el stack
docker compose up -d --build

# 3. Descargar modelos en Ollama (dentro del contenedor)
docker exec -it tfm-ollama ollama pull qwen2.5:3b
docker exec -it tfm-ollama ollama pull nomic-embed-text

# 4. Indexar documentos
docker exec -it tfm-app uv run scripts/setup_and_ingest.py --skip-ollama

# 5. Abrir http://localhost:8501
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
| Ollama sin modelo | `ollama pull qwen2.5:3b && ollama pull nomic-embed-text` |
| Métricas no aparecen | Activar checkbox "📊 Calcular Métricas" en la barra lateral |
| FactScore vacío | Verificar que Ollama esté activo y el modelo descargado |
| Re-indexar | `uv run scripts/setup_and_ingest.py --force-reindex` |
| Error de embeddings | Verificar que `nomic-embed-text` esté descargado en Ollama |

---

## 📄 Documentación Adicional

- [Plan de Hitos del TFM](PLAN_HITOS_TFM.md)
- [Arquitectura y Manual](docs/ARQUITECTURA_Y_MANUAL.md)
- [Protocolo Experimental](docs/protocolo_experimental.md)
- [Definición Matemática de Métricas](docs/METRICAS_IMPLEMENTADAS.md)

---

## 📝 Licencia

Este proyecto es parte de un Trabajo de Fin de Máster académico.
