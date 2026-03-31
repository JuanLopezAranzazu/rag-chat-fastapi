from db.chroma import get_vectorstore

def save_to_db(chunks):
    """Guarda los fragmentos de texto en la base de datos utilizando Chroma VectorStore."""
    vectordb = get_vectorstore()
    vectordb.add_documents(chunks)
    vectordb.persist()