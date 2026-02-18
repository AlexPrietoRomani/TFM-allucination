#!/usr/bin/env python3
"""
setup_and_ingest.py — Script de configuración inicial del proyecto TFM.

Este script automatiza TODO el proceso de primera ejecución:
  1. Verifica que los servicios Docker (Qdrant, Ollama) estén activos.
  2. Descarga el modelo LLM en Ollama si no existe.
  3. Verifica que existan documentos en corpus/raw/.
  4. Indexa los documentos en Qdrant usando el registry.yaml.

Uso:
  uv run scripts/setup_and_ingest.py
  uv run scripts/setup_and_ingest.py --skip-ollama     # Si usas Gemini/OpenRouter
  uv run scripts/setup_and_ingest.py --model qwen2.5:7b # Modelo Ollama diferente
"""

import argparse
import sys
import time
import requests
from pathlib import Path

# Colores para terminal
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def status(msg, ok=True):
    icon = f"{GREEN}✓{RESET}" if ok else f"{RED}✗{RESET}"
    print(f"  {icon} {msg}")

def header(msg):
    print(f"\n{CYAN}{BOLD}{'═' * 60}{RESET}")
    print(f"{CYAN}{BOLD}  {msg}{RESET}")
    print(f"{CYAN}{BOLD}{'═' * 60}{RESET}")


def check_qdrant(url: str) -> bool:
    """Verifica que Qdrant esté activo."""
    try:
        r = requests.get(f"{url}/healthz", timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def check_ollama(url: str) -> bool:
    """Verifica que Ollama esté activo."""
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except Exception:
        return False


def ollama_has_model(url: str, model_name: str) -> bool:
    """Verifica si un modelo ya está descargado en Ollama."""
    try:
        r = requests.get(f"{url}/api/tags", timeout=10)
        if r.status_code == 200:
            models = r.json().get("models", [])
            for m in models:
                if m.get("name", "").startswith(model_name.split(":")[0]):
                    return True
        return False
    except Exception:
        return False


def ollama_pull_model(url: str, model_name: str) -> bool:
    """Descarga un modelo en Ollama (puede tardar varios minutos)."""
    print(f"\n  {YELLOW}⬇ Descargando modelo '{model_name}' en Ollama...{RESET}")
    print(f"  {YELLOW}  (Esto puede tardar varios minutos según tu conexión){RESET}")
    try:
        r = requests.post(
            f"{url}/api/pull",
            json={"name": model_name, "stream": False},
            timeout=600  # 10 minutos máximo
        )
        if r.status_code == 200:
            return True
        else:
            print(f"  {RED}  Error: {r.text}{RESET}")
            return False
    except requests.exceptions.Timeout:
        print(f"  {RED}  Timeout: El modelo es muy grande o la conexión es lenta.{RESET}")
        print(f"  {YELLOW}  Intenta manualmente: ollama pull {model_name}{RESET}")
        return False
    except Exception as e:
        print(f"  {RED}  Error: {e}{RESET}")
        return False


def count_corpus_files() -> tuple:
    """Cuenta archivos en corpus/raw/."""
    raw_dir = Path("corpus/raw")
    if not raw_dir.exists():
        return 0, []
    files = list(raw_dir.glob("*.*"))
    pdfs = [f for f in files if f.suffix.lower() == ".pdf"]
    return len(files), pdfs


def run_indexer():
    """Ejecuta el indexador de documentos."""
    print(f"\n  {YELLOW}📚 Indexando documentos en Qdrant...{RESET}")
    try:
        from src.knowledge.indexer import index_documents
        index_documents()
        return True
    except Exception as e:
        print(f"  {RED}  Error durante indexación: {e}{RESET}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Setup inicial del TFM")
    parser.add_argument("--qdrant-url", default="http://localhost:6333",
                        help="URL de Qdrant (default: http://localhost:6333)")
    parser.add_argument("--ollama-url", default="http://localhost:11434",
                        help="URL de Ollama (default: http://localhost:11434)")
    parser.add_argument("--model", default="qwen2.5:3b",
                        help="Modelo Ollama a descargar (default: qwen2.5:3b)")
    parser.add_argument("--skip-ollama", action="store_true",
                        help="Omitir verificación/descarga de Ollama")
    parser.add_argument("--skip-index", action="store_true",
                        help="Omitir indexación en Qdrant")
    parser.add_argument("--force-reindex", action="store_true",
                        help="Forzar re-indexación (borra colección existente)")
    args = parser.parse_args()

    print(f"\n{BOLD}🫐 TFM-Allucination — Setup Inicial{RESET}")
    print(f"{'─' * 50}")

    # ─── PASO 1: Verificar servicios ─────────────────────────────────────────
    header("PASO 1: Verificando servicios Docker")

    # Qdrant
    if check_qdrant(args.qdrant_url):
        status(f"Qdrant activo en {args.qdrant_url}")
    else:
        status(f"Qdrant NO responde en {args.qdrant_url}", ok=False)
        print(f"\n  {YELLOW}Ejecuta: docker compose up -d qdrant{RESET}")
        print(f"  {YELLOW}Esperando 10s y reintentando...{RESET}")
        time.sleep(10)
        if not check_qdrant(args.qdrant_url):
            print(f"\n  {RED}ERROR: Qdrant no está disponible.{RESET}")
            print(f"  {YELLOW}Inicia los servicios con: docker compose up -d{RESET}")
            sys.exit(1)
        status(f"Qdrant ahora activo en {args.qdrant_url}")

    # Ollama
    if not args.skip_ollama:
        if check_ollama(args.ollama_url):
            status(f"Ollama activo en {args.ollama_url}")

            # Verificar modelo
            if ollama_has_model(args.ollama_url, args.model):
                status(f"Modelo '{args.model}' ya disponible")
            else:
                status(f"Modelo '{args.model}' no encontrado, descargando...", ok=False)
                if ollama_pull_model(args.ollama_url, args.model):
                    status(f"Modelo '{args.model}' descargado correctamente")
                else:
                    print(f"\n  {YELLOW}⚠ No se pudo descargar el modelo automáticamente.{RESET}")
                    print(f"  {YELLOW}  Puedes descargarlo manualmente:{RESET}")
                    print(f"  {YELLOW}  docker exec -it tfm-ollama ollama pull {args.model}{RESET}")
        else:
            status(f"Ollama NO responde en {args.ollama_url}", ok=False)
            print(f"  {YELLOW}Si usas Gemini/OpenRouter, usa --skip-ollama{RESET}")
    else:
        print(f"  ⏭ Ollama omitido (--skip-ollama)")

    # ─── PASO 2: Verificar corpus ────────────────────────────────────────────
    header("PASO 2: Verificando corpus de documentos")

    total_files, pdfs = count_corpus_files()

    if total_files == 0:
        status("No hay documentos en corpus/raw/", ok=False)
        print(f"""
  {YELLOW}Para poblar el corpus, tienes dos opciones:{RESET}

  {BOLD}Opción A: Descargar artículos automáticamente{RESET}
    uv run corpus/fetch_phytosanitary_articles.py   # Batch 1 (30 artículos IA)
    uv run corpus/fetch_phytosanitary_batch2.py      # Batch 2 (30 artículos agro)

  {BOLD}Opción B: Copiar tus propios documentos{RESET}
    1. Crea la carpeta: mkdir corpus/raw
    2. Copia tus PDFs/DOCX/XLSX a corpus/raw/
    3. Actualiza corpus/registry.yaml con los metadatos
    4. Re-ejecuta este script
        """)
        if not args.skip_index:
            print(f"  {YELLOW}Abortando indexación: no hay documentos.{RESET}")
            sys.exit(0)
    else:
        status(f"Encontrados {total_files} archivos ({len(pdfs)} PDFs)")

    # ─── PASO 3: Indexar en Qdrant ───────────────────────────────────────────
    if not args.skip_index:
        header("PASO 3: Indexando documentos en Qdrant")

        if run_indexer():
            status("Indexación completada exitosamente")
        else:
            status("Error durante la indexación", ok=False)
            sys.exit(1)
    else:
        print(f"\n  ⏭ Indexación omitida (--skip-index)")

    # ─── RESUMEN ─────────────────────────────────────────────────────────────
    header("SETUP COMPLETO")
    print(f"""
  {GREEN}✓{RESET} Qdrant:    {args.qdrant_url}
  {GREEN}✓{RESET} Documentos: {total_files} archivos indexados
  {"" if args.skip_ollama else f"{GREEN}✓{RESET} Ollama:    {args.ollama_url} (modelo: {args.model})"}

  {BOLD}Para iniciar la aplicación:{RESET}
    docker compose up -d        # Todo el stack
    uv run streamlit run app.py # Solo la app (desarrollo local)

  {BOLD}Abrir en navegador:{RESET}
    http://localhost:8501
    """)


if __name__ == "__main__":
    main()
