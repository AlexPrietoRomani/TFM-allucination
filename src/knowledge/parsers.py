"""
parsers.py — Pipeline de Parseo Estructurado para PDFs Tabulares

Convierte PDFs complejos (manuales FRAC/IRAC, guías fitosanitarias)
en Markdown estructurado con tablas preservadas y opcionalmente
aplana filas tabulares a oraciones descriptivas para mejorar la
precisión de los embeddings.

Dependencias:
    pip install docling  (o uv add docling)
"""

import re
import logging
from pathlib import Path
from typing import List, Optional, Dict, Any

logger = logging.getLogger(__name__)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. DoclingParser — PDF → Markdown estructurado
# ═══════════════════════════════════════════════════════════════════════════════

class DoclingParser:
    """Convierte un PDF a Markdown usando Docling (IBM).

    Docling reconstruye tablas, headers y layout del PDF respetando
    las Bounding Boxes, produciendo Markdown con tablas intactas.
    """

    def __init__(self):
        # Lazy import para no penalizar el arranque de la app
        try:
            from docling.document_converter import DocumentConverter, PdfFormatOption
            from docling.datamodel.pipeline_options import PdfPipelineOptions
            
            options = PdfPipelineOptions()
            options.do_formula_enrichment = True
            options.generate_picture_images = True
            
            self._converter = DocumentConverter(
                format_options={
                    "pdf": PdfFormatOption(pipeline_options=options)
                }
            )
        except ImportError:
            raise ImportError(
                "docling no está instalado. Ejecuta: uv add docling"
            )

    def parse(self, pdf_path: Path, image_filter: Optional[Any] = None) -> str:
        """Convierte un PDF a Markdown estructurado. Opcionalmente inyecta descripciones VLM.

        Args:
            pdf_path: Ruta al archivo PDF.
            image_filter: Instancia de ImageFilter para describir gráficos.

        Returns:
            String con el contenido en formato Markdown.
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF no encontrado: {pdf_path}")

        logger.info(f"Parseando con Docling: {pdf_path.name}")
        result = self._converter.convert(str(pdf_path))
        doc = result.document

        # 1. Analizar imágenes con VLM consecutivamente si se pasan
        image_descriptions = []
        if image_filter and hasattr(doc, "pictures"):
            logger.info(f"  → Analizando {len(doc.pictures)} imágenes con VLM...")
            for i, pic in enumerate(doc.pictures):
                try:
                    img = pic.get_image(result.document)
                    import io
                    img_byte_arr = io.BytesIO()
                    img.save(img_byte_arr, format='PNG')
                    
                    desc = image_filter.analyze(img_byte_arr.getvalue())
                    image_descriptions.append(desc)
                except Exception as e:
                    logger.warning(f"  → Error procesando imagen {i} en VLM: {e}")
                    image_descriptions.append(None)

        md_content = doc.export_to_markdown()

        # 2. Inyectar descripciones VLM en las etiquetas <!-- image -->
        if image_descriptions:
            count = 0
            def _replace_image(match):
                nonlocal count
                if count < len(image_descriptions):
                    desc = image_descriptions[count]
                    count += 1
                    if desc:
                        return f"\n\n> **[💡 Descripción de Imagen VLM]:** {desc}\n\n"
                return match.group(0)
            
            md_content = re.sub(r"<!--\s*image\s*-->", _replace_image, md_content)

        logger.info(
            f"  → {len(md_content)} caracteres extraídos de {pdf_path.name}"
        )
        return md_content


# ═══════════════════════════════════════════════════════════════════════════════
# 2. TableFlattener — Tablas Markdown → Oraciones descriptivas
# ═══════════════════════════════════════════════════════════════════════════════

class TableFlattener:
    """Transforma tablas Markdown en oraciones descriptivas en lenguaje natural.

    Esto eleva dramáticamente la calidad de los embeddings para documentos
    tabulares como FRAC/IRAC donde cada fila contiene relaciones semánticas
    críticas (ingrediente activo → grupo → código → comentarios).
    """

    # Regex para detectar un bloque de tabla Markdown
    _TABLE_PATTERN = re.compile(
        r"((?:^\|.+\|$\n?)+)",
        re.MULTILINE
    )

    @staticmethod
    def _parse_table_block(table_text: str) -> tuple:
        """Extrae headers y filas de un bloque de tabla Markdown.

        Returns:
            (headers: List[str], rows: List[List[str]])
        """
        lines = [
            line.strip()
            for line in table_text.strip().split("\n")
            if line.strip()
        ]

        if len(lines) < 2:
            return [], []

        # Headers: primera línea
        headers = [
            cell.strip()
            for cell in lines[0].split("|")
            if cell.strip()
        ]

        # Filas: saltar header y separador (línea de guiones)
        rows = []
        for line in lines[2:]:  # Skip header + separator
            # Validar que la línea no sea un separador
            if re.match(r"^\|[\s\-:]+\|$", line):
                continue
            cells = [
                cell.strip()
                for cell in line.split("|")
                if cell.strip()
            ]
            if cells:
                rows.append(cells)

        return headers, rows

    @classmethod
    def flatten(
        cls,
        md_text: str,
        doc_meta: Optional[Dict[str, Any]] = None
    ) -> str:
        """Aplana tablas en el Markdown sustituyéndolas por oraciones descriptivas.

        Args:
            md_text: Contenido Markdown con tablas.
            doc_meta: Metadatos del documento (title, year, tags, etc.)
                      para enriquecer las oraciones.

        Returns:
            Markdown con las tablas reemplazadas por oraciones.
        """
        doc_meta = doc_meta or {}
        doc_title = doc_meta.get("title", "Documento")
        doc_year = doc_meta.get("year", "")

        def _replace_table(match):
            table_text = match.group(0)
            headers, rows = cls._parse_table_block(table_text)

            if not headers or not rows:
                return table_text  # Devolver sin cambios si no se pudo parsear

            sentences = []
            for row in rows:
                # Emparejar cada celda con su header
                pairs = []
                for i, cell in enumerate(row):
                    if i < len(headers) and cell and cell != "-":
                        pairs.append(f"{headers[i]}: {cell}")

                if pairs:
                    prefix = f"Según {doc_title}"
                    if doc_year:
                        prefix += f" ({doc_year})"
                    sentence = f"{prefix}, {', '.join(pairs)}."
                    sentences.append(sentence)

            return "\n".join(sentences) if sentences else table_text

        return cls._TABLE_PATTERN.sub(_replace_table, md_text)


# ═══════════════════════════════════════════════════════════════════════════════
# 3. ImageFilter — Filtrado de imágenes vía VLM local (Ollama)
# ═══════════════════════════════════════════════════════════════════════════════

class ImageFilter:
    """Filtra imágenes decorativas (logos, portadas) y describe las útiles.

    Usa un modelo VLM ligero en Ollama (ej: llava:7b, qwen2-vl) para
    determinar si una imagen contiene información semántica relevante.
    """

    SYSTEM_PROMPT = (
        "Eres un analista experto en extracción de datos científicos. "
        "Analiza esta imagen extraída de un documento. "
        "REGLAS ESTRICTAS:\n"
        "1. Describe de forma concisa qué representa la imagen (gráfico de líneas, diagrama, foto) y su tendencia o conclusión principal.\n"
        "2. NO inventes datos, números ni nombres que no sean legibles.\n"
        "3. NO repitas la misma palabra múltiples veces.\n"
        "4. Si la imagen es un logotipo, un adorno, o texto borroso ilegible, responde EXACTAMENTE con la palabra: DESCARTAR."
    )

    def __init__(
        self,
        model: str = "llama3.2-vision",
        ollama_base_url: str = "http://localhost:11434"
    ):
        self.model = model
        self.base_url = ollama_base_url

    def analyze(self, image_input: Optional[Any] = None) -> Optional[str]:
        """Analiza una imagen y retorna su descripción o None si es decorativa.

        Args:
            image_input: Ruta a la imagen (Path, str) o bytes de la imagen.

        Returns:
            Descripción textual de la imagen, o None si debe descartarse.
        """
        try:
            import ollama
        except ImportError:
            logger.warning("ollama SDK no instalado. Omitiendo análisis de imagen.")
            return None

        if image_input is None:
            return None

        # Resolver payload
        img_payload = image_input
        img_name = "Imagen"
        
        if isinstance(image_input, (str, Path)):
            image_path = Path(image_input)
            if not image_path.exists():
                logger.warning(f"Imagen no encontrada: {image_path}")
                return None
            img_payload = str(image_path)
            img_name = image_path.name

        try:
            client = ollama.Client(host=self.base_url)
            response = client.chat(
                model=self.model,
                messages=[{
                    "role": "user",
                    "content": self.SYSTEM_PROMPT,
                    "images": [img_payload]
                }],
                options={
                    "num_predict": 250,      # Limitar la longitud máxima
                    "temperature": 0.0,      # Eliminamos la creatividad (determinismo total)
                    "top_p": 0.5,            # Reduce el espacio de tokens probables
                    "repeat_penalty": 1.1,   # Penalización suave, suficiente para evitar bucles de palabras normales
                }
            )

            text = response["message"]["content"].strip()
            logger.info(f"DEBUG: VLM {img_name} response raw text = {repr(text)}")

            # Limpieza contra alucinaciones de tokens invisibles y bucles
            import re
            text = text.replace('\xa0', ' ').replace('\xad', '') # Limpiar caracteres invisibles
            text = re.sub(r'([.…] ?){3,}', '...', text) # Colapsar múltiples puntos
            text = re.sub(r'(\s){2,}', ' ', text) # Colapsar múltiples espacios
            text = re.sub(r'(.{5,}?)\1+', r'\1', text) # Detectar y colapsar n-gramas repetidos en bucle
            text = text.strip()

            if "DESCARTAR" in text.upper():
                logger.info(f"  → {img_name} descartada")
                return None

            logger.info(f"  → {img_name} descrita ({len(text)} chars)")
            return text

        except Exception as e:
            logger.warning(f"Error analizando {img_name}: {e}")
            return None
