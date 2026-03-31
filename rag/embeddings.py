from db.chroma import get_vectorstore

def save_to_db(chunks):
    """Guarda los fragmentos de texto en la base de datos utilizando Chroma VectorStore."""
    # Obtener una instancia de Chroma VectorStore
    vectordb = get_vectorstore()
    # Agregar los documentos (fragmentos) a la base de datos y persistir los cambios
    vectordb.add_documents(chunks)
    # Persistir los cambios en la base de datos para asegurarse de que los documentos se guarden correctamente
    vectordb.persist()