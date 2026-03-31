from fastapi import FastAPI
from routes.rag_routes import router
import google.generativeai as genai

app = FastAPI()

app.include_router(router, prefix="/rag")

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de RAG!"}

# Listar los modelos disponibles y sus métodos de generación soportados
for m in genai.list_models():
    print(m.name, m.supported_generation_methods)

