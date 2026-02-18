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

---

## 📂 Estructura del Proyecto

```
TFM-allucination/
├── app.py                          # Aplicación principal Streamlit
├── docker-compose.yml              # Stack completo (Qdrant + Redis + Ollama + App)
├── Dockerfile                      # Imagen de la aplicación
├── pyproject.toml                  # Dependencias (uv)
├── .env.example                    # Variables de entorno (plantilla)
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
│   ├── knowledge/                  # Indexador y cargadores de documentos
│   ├── chat/                       # Motor RAG (V1)
│   ├── agent/                      # Agente autónomo LangGraph (V2)
│   └── metrics/                    # Evaluadores (Fidelidad, FactScore)
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
- **API Key** de Google Gemini (obligatorio para embeddings y como proveedor por defecto)

### Paso 1: Clonar y Configurar Variables de Entorno

```bash
git clone https://github.com/TU_USUARIO/TFM-allucination.git
cd TFM-allucination

# Copiar plantilla y editar con tus API keys
cp .env.example .env
# Editar .env con tu editor favorito
```

> **⚠️ Importante:** Necesitas al menos `GOOGLE_API_KEY` configurada, ya que se usa para los embeddings (Text-Embedding-004) y como proveedor LLM por defecto.

### Paso 2: Instalar Dependencias Python

```bash
# Instalar uv si no lo tienes
pip install uv

# Instalar dependencias del proyecto
uv sync
```

### Paso 3: Levantar la Infraestructura Docker

```bash
# Levanta Qdrant, Redis y Ollama
docker compose up -d
```

Esto inicia tres servicios:
- **Qdrant** (puerto 6333) — Base de datos vectorial
- **Redis** (puerto 6379) — Cola de tareas y caché
- **Ollama** (puerto 11434) — LLM local

Verifica que estén activos:
```bash
docker compose ps
```

### Paso 4: Obtener Documentos del Corpus

Los documentos PDF **no se incluyen en el repositorio** (están en `.gitignore`). Debes obtenerlos de alguna de estas formas:

#### Opción A: Descarga Automática desde ArXiv (Recomendado)

```bash
# Batch 1: 30 artículos de detección de plagas/enfermedades con IA
uv run corpus/fetch_phytosanitary_articles.py

# Batch 2: 30 artículos de agronomía de campo (control biológico, fungicidas, etc.)
uv run corpus/fetch_phytosanitary_batch2.py
```

Cada script:
- Descarga los PDFs en `corpus/raw/`
- Actualiza `corpus/registry.yaml` con metadatos
- Genera CSVs de seguimiento en `corpus/`

#### Opción B: Documentos Propios

```bash
# 1. Crear la carpeta si no existe
mkdir -p corpus/raw

# 2. Copiar tus documentos (PDF, DOCX, XLSX)
cp /ruta/a/tus/documentos/*.pdf corpus/raw/

# 3. Registrarlos en corpus/registry.yaml (ver formato abajo)
```

### Paso 5: Setup Automático (Indexación + Modelo Ollama)

El script `setup_and_ingest.py` automatiza todo el proceso:

```bash
uv run scripts/setup_and_ingest.py
```

Este script:
1. ✅ Verifica que Qdrant y Ollama estén activos
2. ✅ Descarga el modelo `qwen2.5:3b` en Ollama (1.9 GB, si no existe)
3. ✅ Verifica que haya documentos en `corpus/raw/`
4. ✅ Indexa todos los documentos en la base vectorial Qdrant

**Opciones adicionales:**
```bash
# Si solo usas Gemini/OpenRouter (sin LLM local):
uv run scripts/setup_and_ingest.py --skip-ollama

# Para usar un modelo Ollama diferente:
uv run scripts/setup_and_ingest.py --model qwen2.5:7b

# Solo verificar servicios, sin indexar:
uv run scripts/setup_and_ingest.py --skip-index

# Forzar re-indexación completa:
uv run scripts/setup_and_ingest.py --force-reindex
```

### Paso 6: Iniciar la Aplicación

```bash
# Opción A: Ejecución local (desarrollo)
uv run streamlit run app.py

# Opción B: Con Docker (producción)
docker compose up -d --build
```

La aplicación estará disponible en: **http://localhost:8501**

---

## 🐋 Despliegue Completo con Docker

Para levantar **todo el stack** (App + Qdrant + Redis + Ollama) con un solo comando:

```bash
# 1. Configurar variables de entorno
cp .env.example .env
# Editar .env con tus API keys

# 2. Levantar todo el stack
docker compose up -d --build

# 3. Descargar modelo Ollama (dentro del contenedor)
docker exec -it tfm-ollama ollama pull qwen2.5:3b

# 4. Indexar documentos (requiere que corpus/raw/ tenga archivos)
docker exec -it tfm-app uv run scripts/setup_and_ingest.py --skip-ollama

# 5. Abrir http://localhost:8501
```

### Modelos Ollama Recomendados

| Modelo | Tamaño | Parámetros | Ideal para |
|--------|--------|------------|------------|
| `qwen2.5:3b` | 1.9 GB | 3B | ⭐ **Recomendado** — Mejor relación calidad/tamaño |
| `qwen2.5:7b` | 4.7 GB | 7B | Mayor calidad, requiere más RAM |
| `phi3:mini` | 2.3 GB | 3.8B | Buen razonamiento lógico |
| `gemma2:2b` | 1.6 GB | 2B | Ultra-ligero, respuestas rápidas |

---

## 📚 Gestión del Corpus de Conocimiento

### Estructura del `registry.yaml`

Cada documento en `corpus/raw/` debe tener una entrada correspondiente en `corpus/registry.yaml`:

```yaml
documents:
  - id: arxiv-2504.07342           # ID único (nombre del archivo sin extensión)
    title: "Título del documento"
    url: "https://arxiv.org/abs/2504.07342"
    type: pdf                       # pdf, docx, xlsx
    language: en                    # en, es
    tags:
      - detección de enfermedades
      - deep learning
      - arándanos
    description: "Descripción breve del contenido..."
    year: 2025
    country: Internacional
    source: "ArXiv (cs.CV)"
    doc_type: "Artículo científico"
    checksum: "sha256..."          # Opcional
```

### Agregar Nuevos Documentos

#### Paso a paso para agregar artículos manualmente:

1. **Copiar el archivo** a `corpus/raw/`:
   ```bash
   cp mi_articulo.pdf corpus/raw/mi-articulo-id.pdf
   ```

2. **Agregar entrada en `corpus/registry.yaml`**:
   ```yaml
   # Añadir al final de la lista 'documents:'
   - id: mi-articulo-id
     title: "Título de mi artículo"
     url: "https://doi.org/..."
     type: pdf
     language: es
     tags:
       - fitosanidad
       - arándanos
     description: "Breve descripción..."
     year: 2024
     country: Chile
     source: "Revista XYZ"
     doc_type: "Artículo científico"
   ```

3. **Re-indexar en Qdrant**:
   ```bash
   uv run scripts/setup_and_ingest.py
   ```
   > ⚠️ Esto **recrea** la colección y re-indexa TODOS los documentos. Es seguro ejecutarlo múltiples veces.

#### Para agregar artículos desde ArXiv automáticamente:

1. **Editar la lista de IDs** en el script correspondiente o en `corpus/curated_arxiv_ids.json`
2. **Ejecutar el script**:
   ```bash
   uv run corpus/fetch_phytosanitary_batch2.py
   ```
3. **Re-indexar**:
   ```bash
   uv run scripts/setup_and_ingest.py
   ```

#### Para crear un nuevo batch de artículos:

1. Crea un nuevo script basado en `fetch_phytosanitary_batch2.py`
2. Define los IDs de ArXiv curados
3. El script automáticamente:
   - Descarga PDFs solo de artículos nuevos
   - Actualiza `registry.yaml` sin duplicados
   - Genera CSVs de seguimiento

### Verificar el Estado de la Indexación

```bash
# Verificar qué documentos están indexados en Qdrant
uv run scripts/verify_ingestion.py
```

---

## 🖥️ Uso de la Aplicación

La aplicación tiene 5 pestañas principales:

| Pestaña | Función |
|---------|---------|
| ⚔️ **Comparativa** | Compara respuestas V0 vs V1, V1 vs V2, o V0 vs V2 lado a lado |
| 🧠 **V0 (Baseline)** | Chat directo con el LLM sin contexto |
| 📚 **V1 (RAG)** | Chat con recuperación de documentos + métricas de calidad |
| 🤖 **V2 (Agente)** | Agente autónomo con pasos de razonamiento visibles |
| 📊 **Reportes** | Ejecutar benchmarks y generar informes comparativos |

### Configuración desde la Barra Lateral

- **Proveedor LLM**: Gemini, OpenRouter, o Ollama
- **Modelo**: Seleccionable según el proveedor
- **Métricas**: Activar cálculo de Fidelidad / Relevancia / FactScore

---

## 📊 Evaluación y Benchmarks

Para replicar los resultados experimentales del TFM:

```bash
# Evaluación V0 y V1
uv run eval/run_eval.py

# Evaluación V2 (Agente)
uv run eval/run_eval_v2.py

# Métricas V1 (Faithfulness / FactScore)
uv run eval/run_metrics.py
uv run eval/run_factscore.py

# Generar reporte unificado
uv run reports/generate_report.py --mode all
```

Los reportes se guardan en `reports/`.

---

## 🔧 Troubleshooting

### Qdrant no responde
```bash
docker compose restart qdrant
# Verificar logs:
docker compose logs qdrant
```

### Ollama sin modelo
```bash
# Descargar modelo manualmente:
docker exec -it tfm-ollama ollama pull qwen2.5:3b

# O con Ollama local (fuera de Docker):
ollama pull qwen2.5:3b
```

### Error de embeddings / API Key
Verifica que tu `.env` tenga `GOOGLE_API_KEY` configurada correctamente. Los embeddings requieren esta clave incluso si usas Ollama como LLM.

### Re-indexar documentos
```bash
uv run scripts/setup_and_ingest.py --force-reindex
```

### La app no encuentra documentos
1. Verifica que `corpus/raw/` contenga archivos
2. Verifica que `corpus/registry.yaml` tenga entradas
3. Ejecuta el setup: `uv run scripts/setup_and_ingest.py`

---

## 📄 Documentación Adicional

- [Arquitectura y Manual](docs/ARQUITECTURA_Y_MANUAL.md)
- [Protocolo Experimental](docs/protocolo_experimental.md)
- [Definición Matemática de Métricas](docs/METRICAS_IMPLEMENTADAS.md)
- [Plan de Hitos](plan_hitos_chatbot_llm_rag_metricas.md)

---

## 📝 Licencia

Este proyecto es parte de un Trabajo de Fin de Máster académico.
