# TFM: Mitigación de Alucinaciones en LLMs Agrícolas

Este repositorio contiene la implementación del Trabajo de Fin de Máster sobre la mitigación y medición de alucinaciones en Modelos de Lenguaje aplicados a la agricultura (caso de uso: Arándanos).

El sistema compara tres enfoques:
- **V0 (Baseline)**: Chat estándar.
- **V1 (RAG)**: Retrieval-Augmented Generation.
- **V2 (Agente Autónomo)**: Sistema con LangGraph y ciclos de auto-corrección.

## 🚀 Despliegue e Instalación

### Prerrequisitos
- **Python 3.10+** (Recomendado usar `uv` para gestión)
- **Docker & Docker Compose** (Para Qdrant y Redis)
- **API Keys**: Google Gemini o OpenRouter.

### Paso 1: Configurar Entorno

1.  Clonar el repositorio.
2.  Copiar el archivo de entorno y configurarlo:
    ```bash
    cp .env.example .env
    # Editar .env con tus API KEYS
    ```
3.  Instalar dependencias con `uv`:
    ```bash
    uv sync
    ```

### Paso 2: Iniciar Servicios (Stack Completo)

Puede iniciar todo el sistema (App + Worker + BD + Ollama) con un solo comando:
```bash
docker-compose up -d --build
```

**Nota sobre Ollama**:
- El servicio `ollama` incluido iniciará vacío.
- Para descargar el modelo requerido dentro del contenedor:
  ```bash
  docker exec -it tfm-ollama ollama pull gpt-oss:20b
  ```
- Si prefiere usar su Ollama local (Windows/Mac), modifique `docker-compose.yml` para apuntar a `host.docker.internal`.

### Paso 3: Ingestar Conocimiento

Antes de usar el chat, debe indexar los documentos en Qdrant (ahora corriendo en Docker):
```bash
# Ejecutar el script dentro del contenedor de la app
docker exec -it tfm-app uv run src/knowledge/indexer.py
```

---

## 🖥️ Ejecución de la Aplicación

La aplicación estará disponible automáticamente en:
👉 **http://localhost:8501**

### Nuevas Funcionalidades (Hito 15)
- **Pestaña "📊 Reportes & Eval"**: Ejecute benchmarks V0/V1/V2 directamente desde la interfaz.
- **Barra de Progreso**: Visualice el avance de la evaluación en tiempo real.
- **Generación de PDF/Markdwn**: Descargue los resultados comparativos con un clic.

---

## 📊 Evaluación y Benchmarks (Reproducibilidad)

Para replicar los resultados experimentales del TFM (V0 vs V1 vs V2):

### 1. Ejecutar Evaluación
Genera respuestas para el Banco de Preguntas (`eval/question_bank_v1.csv`):

**Para V0 y V1:**
```bash
uv run eval/run_eval.py
```

**Para V2 (Agente):**
```bash
uv run eval/run_eval_v2.py
```

**Calcular Métricas V1 (Faithfulness/FactScore):**
```bash
uv run eval/run_metrics.py
uv run eval/run_factscore.py
```

### 2. Generar Reporte Unificado
Consolida todos los resultados en un único archivo Markdown comparativo:
```bash
# Reporte Completo (V0, V1, V2)
uv run reports/generate_report.py --mode all

# Solo Agente V2
uv run reports/generate_report.py --mode v2
```
Los reportes se guardan en `reports/`.

---

## 📂 Estructura del Proyecto

Ver detalles completos en [docs/ARQUITECTURA_Y_MANUAL.md](docs/ARQUITECTURA_Y_MANUAL.md).

- **`src/agent/`**: Lógica del Agente V2 (LangGraph, Nodos, Estado).
- **`src/chat/`**: Lógica del RAG V1.
- **`src/metrics/`**: Implementación de evaluadores (Fidelidad, FactScore).
- **`services/worker/`**: Tareas asíncronas.
- **`eval/`**: Scripts de benchmarking y datos de prueba.

---

## 📄 Documentación Adicional
- [Arquitectura y Manual](docs/ARQUITECTURA_Y_MANUAL.md)
- [Protocolo Experimental](docs/protocolo_experimental.md)
- [Definición Matemática de Métricas](docs/METRICAS_IMPLEMENTADAS.md)
