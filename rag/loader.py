from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import settings

def load_and_split(file_path):
    """Carga un archivo PDF, lo divide en fragmentos de texto y devuelve una lista de documentos."""
    # Cargar el archivo PDF utilizando PyPDFLoader
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    # Dividir los documentos en fragmentos de texto utilizando RecursiveCharacterTextSplitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap
    )
    # Dividir los documentos en fragmentos y devolver la lista de fragmentos resultante
    chunks = splitter.split_documents(docs)
    return chunks