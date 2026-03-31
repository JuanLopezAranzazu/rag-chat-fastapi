from db.chroma import get_vectorstore

def get_retriever():
    """Crea y devuelve un sistema de recuperación de documentos utilizando Chroma VectorStore."""
    vectordb = get_vectorstore()
    return vectordb.as_retriever(search_kwargs={"k": 3})