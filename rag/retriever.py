from db.chroma import get_vectorstore
from config import settings

def get_retriever():
    """Crea y devuelve un sistema de recuperación de documentos utilizando Chroma VectorStore."""
    # Obtener una instancia de Chroma VectorStore
    vectordb = get_vectorstore()
    # Devolver un sistema de recuperación basado en el VectorStore con parámetros de búsqueda configurados
    return vectordb.as_retriever(search_kwargs={"k": settings.top_k})