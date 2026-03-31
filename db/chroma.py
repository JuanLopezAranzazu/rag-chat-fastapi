from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from config import settings

def get_vectorstore():
    """Crea y devuelve una instancia de Chroma VectorStore utilizando HuggingFaceEmbeddings."""
    # Configurar la función de embeddings utilizando un modelo preentrenado de HuggingFace
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # Crear una instancia de Chroma VectorStore con el directorio de persistencia y la función de embeddings configurada
    vectordb = Chroma(
        persist_directory=settings.chroma_db_path,
        embedding_function=embeddings
    )

    return vectordb