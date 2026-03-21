import ollama
from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

SYSTEM_PROMPT = (
    "Analiza esta imagen en el contexto de un documento técnico agrícola. "
    "Si es solo un logo institucional, gráfico decorativo, portada o "
    "elemento sin información técnica, responde ÚNICAMENTE: DESCARTAR. "
    "Si es un diagrama de flujo, esquema químico, tabla visual, mapa, "
    "ciclo de vida de plaga o gráfico con datos, descríbelo "
    "detalladamente en español para que un sistema de búsqueda pueda "
    "encontrar esta información."
)

def analyze_vlm_image(image_bytes, model="llama3.2-vision", base_url="http://localhost:11434"):
    """Llama a Ollama para describir una imagen."""
    try:
        client = ollama.Client(host=base_url)
        # image_bytes puede ser un buffer u objeto bytes
        response = client.chat(
            model=model,
            messages=[{
                "role": "user",
                "content": SYSTEM_PROMPT,
                "images": [image_bytes]
            }]
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return f"Error VLM: {e}"

def main():
    pdf_path = Path("corpus/raw/arxiv-2205.07723.pdf")
    if not pdf_path.exists():
         print(f"No se encontró el PDF {pdf_path}")
         return

    print(f"--- 1. Ejecutando Docling para: {pdf_path.name} ---")
    
    options = PdfPipelineOptions()
    options.generate_picture_images = True # Enciende recortes de imágenes
    options.do_formula_enrichment = True  # Enciende modelo de ecuaciones
    
    converter = DocumentConverter(
        format_options={
            "pdf": PdfFormatOption(pipeline_options=options)
        }
    )
    
    result = converter.convert(str(pdf_path))
    doc = result.document

    # 2. Iterar sobre imágenes con VLM
    print("\n--- 2. Analizando Imágenes con Llama3.2-Vision ---")
    image_descriptions = []
    if hasattr(doc, "pictures"):
        for i, pic in enumerate(doc.pictures):
            try:
                # Obtener PIL.Image
                img = pic.get_image(result.document)
                
                # Guardar en buffer Bytes para pasar a Ollama
                import io
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format='PNG')
                img_bytes = img_byte_arr.getvalue()

                print(f" -> Procesando Imagen {i} ({img.size})...")
                desc = analyze_vlm_image(img_bytes)
                if "DESCARTAR" in desc.upper():
                     print(f"    - [\u274C Descartada]")
                     image_descriptions.append(None)
                else:
                     print(f"    - [\u2705 Descrita]: {desc[:100]}...")
                     image_descriptions.append(desc)
            except Exception as e:
                print(f" -> Error Imagen {i}: {e}")
                image_descriptions.append(None)

    # 3. Exportar a Markdown y Fusionar
    md_content = doc.export_to_markdown()
    
    if image_descriptions:
         print("\n--- 3. Fusionando Descripciones VLM en el Markdown ---")
         # Reemplazar secuencialmente <!-- image --> de forma segura
         # (Se asume que el orden de Pictures coincide con el de etiquetas en el MD)
         count = 0
         def _replace_image(match):
              nonlocal count
              if count < len(image_descriptions):
                   desc = image_descriptions[count]
                   count += 1
                   if desc:
                        return f"\n\n> **[💡 Descripción de Imagen VLM]:** {desc}\n\n"
              return match.group(0) # Si no hay descripcion, se queda tal cual
         
         import re
         # Regex para capturar <!-- image --> o formato figura
         md_content = re.sub(r"<!--\s*image\s*-->", _replace_image, md_content)

    # 4. Guardar resultado de prueba
    output_path = Path("tests/result_arxiv_vlm.md")
    output_path.write_text(md_content, encoding="utf-8")
    print(f"\n--- ✅ Éxito: Guardado en {output_path} ---")

if __name__ == "__main__":
    main()
