"""
preprocess_corpus.py — Orquestador de Pre-procesamiento de Corpus

Lee corpus/registry.yaml, convierte cada PDF a Markdown estructurado usando Docling
(con soporte para fórmulas LaTeX), aplana tablas a oraciones descriptivas amigables
para embeddings, analiza imágenes técnicas vía VLM (Ollama) e inyecta metadatos YAML.

El resultado se guarda en corpus/parsed/{doc_id}.md

Uso:
    uv run python scripts/preprocess_corpus.py [OPCIONES]

Opciones:
    --skip-images   Omitir el análisis de imágenes con VLM (proceso mucho más rápido).
    --no-flatten    Conservar tablas en formato Markdown puro (sin aplanar a oraciones).
    --force         Forzar el reprocesamiento de archivos aunque ya existan en corpus/parsed/.
    --only-ids ID   Procesar solo IDs específicos separados por coma (ej: --only-ids id1,id2).
    --limit N       Procesar un número máximo fijo de N documentos.
"""

import argparse
import logging
import sys
import yaml
from pathlib import Path
from tqdm import tqdm

# Añadir raíz del proyecto al path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.knowledge.parsers import DoclingParser, TableFlattener, ImageFilter

# ── Configuración ────────────────────────────────────────────────────────────
REGISTRY_PATH = Path("corpus/registry.yaml")
RAW_DIR = Path("corpus/raw")
PARSED_DIR = Path("corpus/parsed")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def load_registry() -> list:
    """Carga la lista de documentos del registry."""
    if not REGISTRY_PATH.exists():
        logger.error(f"Registry no encontrado: {REGISTRY_PATH}")
        return []
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("documents", [])


def find_raw_file(doc_id: str) -> Path | None:
    """Busca el archivo raw correspondiente a un doc_id."""
    candidates = list(RAW_DIR.glob(f"{doc_id}.*"))
    if not candidates:
        return None
    return candidates[0]


def build_metadata_header(doc_meta: dict) -> str:
    """Genera un header YAML-front-matter para el Markdown procesado."""
    lines = ["---"]
    for key in ["id", "title", "year", "country", "source", "doc_type", "language"]:
        val = doc_meta.get(key, "")
        if val:
            lines.append(f"{key}: {val}")

    tags = doc_meta.get("tags", [])
    if tags:
        lines.append("tags:")
        for tag in tags:
            lines.append(f"  - {tag}")

    lines.append("---")
    return "\n".join(lines)


def preprocess_document(
    doc_meta: dict,
    parser: DoclingParser,
    flatten_tables: bool = True,
    image_filter: ImageFilter | None = None,
) -> str | None:
    """Procesa un único documento: PDF → Markdown → Flatten → Metadata.

    Returns:
        Contenido Markdown procesado, o None si falla.
    """
    doc_id = doc_meta["id"]
    file_path = find_raw_file(doc_id)

    if file_path is None:
        logger.warning(f"SALTAR: Archivo para '{doc_id}' no encontrado en {RAW_DIR}")
        return None

    suffix = file_path.suffix.lower()

    # Solo procesamos PDFs con Docling. DOCX/XLSX mantienen flujo original.
    if suffix != ".pdf":
        logger.info(f"SALTAR Docling: {doc_id} es {suffix} (no PDF)")
        return None

    try:
        # 1. PDF → Markdown con Docling (con VLM si aplica)
        md_content = parser.parse(file_path, image_filter=image_filter)

        if not md_content or len(md_content.strip()) < 50:
            logger.warning(f"Contenido vacío/muy corto para {doc_id}")
            return None

        # 2. Aplanar tablas → oraciones descriptivas
        if flatten_tables:
            md_content = TableFlattener.flatten(md_content, doc_meta)

        # 3. Inyectar metadatos como front-matter YAML
        header = build_metadata_header(doc_meta)
        full_content = f"{header}\n\n{md_content}"

        return full_content

    except Exception as e:
        logger.error(f"ERROR procesando {doc_id}: {e}")
        return None


def main():
    arg_parser = argparse.ArgumentParser(
        description="Pre-procesa el corpus de PDFs a Markdown estructurado"
    )
    arg_parser.add_argument(
        "--skip-images",
        action="store_true",
        help="Omitir análisis de imágenes con VLM (más rápido)"
    )
    arg_parser.add_argument(
        "--no-flatten",
        action="store_true",
        help="No aplanar tablas a oraciones (conservar Markdown puro)"
    )
    arg_parser.add_argument(
        "--only-ids",
        type=str,
        default=None,
        help="Procesar solo estos IDs separados por coma"
    )
    arg_parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Límite máximo de documentos a procesar"
    )
    arg_parser.add_argument(
        "--force",
        action="store_true",
        help="Forzar reprocesamiento incluso si el archivo ya existe"
    )
    args = arg_parser.parse_args()

    # Crear directorio de salida
    PARSED_DIR.mkdir(parents=True, exist_ok=True)

    # Cargar registry
    documents = load_registry()
    if not documents:
        logger.error("No se encontraron documentos en el registry")
        return

    # Filtrar por IDs específicos si se solicitó
    if args.only_ids:
        target_ids = set(args.only_ids.split(","))
        documents = [d for d in documents if d["id"] in target_ids]
        logger.info(f"Filtrado a {len(documents)} documentos: {target_ids}")

    # Filtrar solo PDFs (Docling no procesa XLSX/DOCX)
    pdf_docs = [d for d in documents if d.get("type", "pdf") == "pdf"]
    
    # Aplicar límite si se especifica
    if args.limit:
        pdf_docs = pdf_docs[:args.limit]
        logger.info(f"Límite aplicado: Se procesarán sólo {len(pdf_docs)} documentos")
    else:
        logger.info(f"Documentos PDF a procesar: {len(pdf_docs)} de {len(documents)} total")

    # Inicializar parser
    logger.info("Inicializando Docling Parser...")
    parser = DoclingParser()

    # ImageFilter (opcional)
    image_filter = None
    if not args.skip_images:
        try:
            image_filter = ImageFilter()
            logger.info("ImageFilter activado (VLM: llama3.2-vision)")
        except Exception as e:
            logger.warning(f"ImageFilter no disponible: {e}. Continuando sin imágenes.")

    # Procesar cada documento
    success_count = 0
    skip_count = 0
    error_count = 0

    for doc_meta in tqdm(pdf_docs, desc="Procesando PDFs"):
        doc_id = doc_meta["id"]
        output_path = PARSED_DIR / f"{doc_id}.md"

        # Si ya existe, saltar (usar --force para reprocesar)
        if output_path.exists() and not getattr(args, 'force', False):
            logger.info(f"  Ya existe: {output_path.name} (saltando)")
            skip_count += 1
            continue

        result = preprocess_document(
            doc_meta=doc_meta,
            parser=parser,
            flatten_tables=not args.no_flatten,
            image_filter=image_filter,
        )

        if result is None:
            error_count += 1
            continue

        # Guardar
        output_path.write_text(result, encoding="utf-8")
        logger.info(f"  ✅ Guardado: {output_path.name} ({len(result)} chars)")
        success_count += 1

    # Resumen
    print(f"\n{'═' * 60}")
    print(f"  RESUMEN DE PRE-PROCESAMIENTO")
    print(f"{'═' * 60}")
    print(f"  ✅ Procesados exitosamente: {success_count}")
    print(f"  ⏭️  Saltados (ya existían):  {skip_count}")
    print(f"  ❌ Errores/no encontrados:  {error_count}")
    print(f"  📁 Directorio de salida:    {PARSED_DIR.resolve()}")
    print(f"{'═' * 60}")


if __name__ == "__main__":
    main()
