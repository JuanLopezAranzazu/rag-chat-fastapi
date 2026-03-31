from fastapi import FastAPI
from routes.rag_routes import router
import google.generativeai as genai

# Crear la aplicación FastAPI
app = FastAPI()
# Incluir las rutas del router de RAG
app.include_router(router, prefix="/rag")

# Ruta raíz para verificar que la API está funcionando
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de RAG!"}

# Listar los modelos disponibles y sus métodos de generación soportados
for m in genai.list_models():
    print(m.name, m.supported_generation_methods)


# Middleware para manejar errores globales
@app.middleware("http")
async def add_process_time_header(request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        return {"error": str(e)}

