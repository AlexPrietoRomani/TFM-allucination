from pathlib import Path
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import PdfPipelineOptions

def main():
    pdf_path = Path("corpus/raw/frac-code-list-2024.pdf") # Un PDF que exista
    if not pdf_path.exists():
        # Tomar el primero que haya
        candidates = list(Path("corpus/raw").glob("*.pdf"))
        if candidates:
            pdf_path = candidates[0]
        else:
            print("No hay PDFs en corpus/raw")
            return

    print(f"Probando Docling con imágenes en: {pdf_path}")
    
    options = PdfPipelineOptions()
    options.generate_page_images = True # Captura imágenes de página entera si fuesen necesarias
    
    converter = DocumentConverter(
        format_options={
            "pdf": PdfFormatOption(pipeline_options=options)
        }
    )
    
    result = converter.convert(str(pdf_path))
    doc = result.document

    print("\n--- Estructura del Documento ---")
    print(f"Título: {getattr(doc, 'title', 'N/A')}")
    
    # Revisar si se extraen figuras/imágenes
    if hasattr(doc, "pictures"):
        print(f"\nImágenes/Pictures encontradas: {len(doc.pictures)}")
        for i, pic in enumerate(doc.pictures):
            print(f"--- Imagen {i} ---")
            print(f"Atributos de la Imagen: {dir(pic)}")
            # Intentar ver si tiene imagen
            if hasattr(pic, "image"):
                print(f"Tipo .image: {type(pic.image)}")
            elif hasattr(pic, "get_image"):
                 print("Tiene get_image()")
            break # Solo la primera
    else:
        print("No tiene atributo 'pictures'")

if __name__ == "__main__":
    main()
