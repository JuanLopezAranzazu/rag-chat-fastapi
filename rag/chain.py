from dotenv import load_dotenv
import google.generativeai as genai
import os
from rag.retriever import get_retriever

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Verificar que la clave de API esté presente
if not api_key:
    raise ValueError("No se encontró GOOGLE_API_KEY en el entorno")

# Configurar la clave de API para Google Generative AI
genai.configure(api_key=api_key)
# Crear una instancia del modelo generativo que se utilizará para responder preguntas
model = genai.GenerativeModel("gemini-2.5-flash")

def ask_question(query):
    """Responde a una pregunta utilizando un modelo generativo y un sistema de recuperación de documentos."""
    # Obtener documentos relevantes utilizando el sistema de recuperación
    retriever = get_retriever()
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Responde usando SOLO este contexto:

    {context}

    Pregunta: {query}
    """

    response = model.generate_content(prompt)
    return response.text