import pandas as pd
from typing import List
from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader

class DocumentLoader:
    @staticmethod
    def load_pdf(file_path: Path) -> List[Document]:
        loader = PyPDFLoader(str(file_path))
        return loader.load()

    @staticmethod
    def load_docx(file_path: Path) -> List[Document]:
        # Docx2txtLoader usa docx2txt bajo el capó
        loader = Docx2txtLoader(str(file_path))
        return loader.load()

    @staticmethod
    def load_xlsx(file_path: Path) -> List[Document]:
        """
        Carga un archivo Excel usando pandas y convierte cada hoja a una representación markdown.
        """
        docs = []
        try:
            xls = pd.ExcelFile(file_path)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                # Convertir a formato genérico markdown
                # Rellenar NaNs para evitar tablas rotas
                df = df.fillna("")
                text_content = f"# Hoja: {sheet_name}\n\n"
                try:
                    text_content += df.to_markdown(index=False)
                except ImportError:
                    # fallback si tabulate no está instalado, aunque deberíamos tenerlo
                    text_content += df.to_string(index=False)
                
                # Crear un documento por cada hoja (o podría ser 1 doc por archivo)
                # Un doc por hoja suele ser mejor para la relevancia de recuperación.
                docs.append(Document(
                    page_content=text_content,
                    metadata={"source": str(file_path), "sheet": sheet_name}
                ))
        except Exception as e:
            print(f"Error cargando Excel {file_path}: {e}")
        return docs

    @staticmethod
    def load_document(file_path: Path, doc_id: str = None, extra_metadata: dict = None) -> List[Document]:
        """
        Cargador unificado que despacha según la extensión del archivo y enriquece los metadatos.
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
        
        suffix = file_path.suffix.lower()
        docs = []
        
        if suffix == ".pdf":
            docs = DocumentLoader.load_pdf(file_path)
        elif suffix in [".docx", ".doc"]:
            docs = DocumentLoader.load_docx(file_path)
        elif suffix in [".xlsx", ".xls"]:
            docs = DocumentLoader.load_xlsx(file_path)
        else:
            print(f"Tipo de archivo no soportado: {suffix}")
            return []
            
        # Enriquecer metadatos
        for i, doc in enumerate(docs):
            if doc_id:
                doc.metadata["doc_id"] = doc_id
            
            # Asegurar metadatos comunes básicos
            doc.metadata["filename"] = file_path.name
            doc.metadata["file_extension"] = suffix
            
            if extra_metadata:
                doc.metadata.update(extra_metadata)
                
        return docs
