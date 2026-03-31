import google.generativeai as genai
from rag.retriever import get_retriever
from config import settings

# Configurar la clave de API para Google Generative AI
genai.configure(api_key=settings.google_api_key)
# Crear una instancia del modelo generativo que se utilizará para responder preguntas
model = genai.GenerativeModel(settings.llm_model)

def ask_question(query):
    """Responde a una pregunta utilizando un modelo generativo y un sistema de recuperación de documentos."""
    # Obtener documentos relevantes utilizando el sistema de recuperación
    retriever = get_retriever()
    docs = retriever.invoke(query)
    # Construir el contexto a partir de los documentos recuperados
    context = "\n\n".join([
        f"[Fragmento {i+1}]\n{doc.page_content}"
        for i, doc in enumerate(docs)
    ])
    # Construir el prompt para el modelo generativo, incluyendo el rol, las reglas, el contexto y la pregunta
    prompt = f"""
    Rol: Asistente experto en análisis documental.

    Reglas:
    - Usa solo el contexto
    - No inventes
    - Si no sabes, dilo

    Contexto:
    {context}

    Pregunta:
    {query}

    Respuesta:
    """
    # Generar la respuesta utilizando el modelo generativo
    response = model.generate_content(prompt)
    return response.text