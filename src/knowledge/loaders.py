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
        loader = Docx2txtLoader(str(file_path))
        return loader.load()

    @staticmethod
    def load_xlsx(file_path: Path) -> List[Document]:
        """
        Loads Excel file using pandas and converts each sheet to a markdown representation.
        """
        docs = []
        try:
            xls = pd.ExcelFile(file_path)
            for sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name=sheet_name)
                # Convert to markdown generic format
                text_content = f"# Sheet: {sheet_name}\n\n"
                text_content += df.to_markdown(index=False)
                
                # Create a document for each sheet (or could be 1 doc for file)
                # One doc per sheet is often better for retrieval relevance.
                docs.append(Document(
                    page_content=text_content,
                    metadata={"source": str(file_path), "sheet": sheet_name}
                ))
        except Exception as e:
            print(f"Error loading Excel {file_path}: {e}")
        return docs

    @staticmethod
    def load_document(file_path: Path, doc_id: str = None, extra_metadata: dict = None) -> List[Document]:
        """
        Unified loader that dispatches based on file extension and enriches metadata.
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        suffix = file_path.suffix.lower()
        docs = []
        
        if suffix == ".pdf":
            docs = DocumentLoader.load_pdf(file_path)
        elif suffix in [".docx", ".doc"]:
            docs = DocumentLoader.load_docx(file_path)
        elif suffix in [".xlsx", ".xls"]:
            docs = DocumentLoader.load_xlsx(file_path)
        else:
            print(f"Unsupported file type: {suffix}")
            return []
            
        # Enrich metadata
        for i, doc in enumerate(docs):
            if doc_id:
                doc.metadata["doc_id"] = doc_id
            
            # Ensure basic common metadata
            doc.metadata["filename"] = file_path.name
            doc.metadata["file_extension"] = suffix
            
            if extra_metadata:
                doc.metadata.update(extra_metadata)
                
        return docs
