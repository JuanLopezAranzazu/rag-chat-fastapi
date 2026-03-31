from dotenv import load_dotenv
import os

class Settings:
    """Clase para cargar y almacenar configuraciones de la aplicación."""
    def __init__(self):
        # Cargar variables de entorno
        load_dotenv()

        # API KEYS
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        # Verificar que la clave de API esté presente
        if not self.google_api_key:
            raise ValueError("No se encontró GOOGLE_API_KEY en el entorno")
        
        # LLM
        self.llm_model = os.getenv("LLM_MODEL", "gemini-2.5-flash")

        # RAG
        self.chunk_size = int(os.getenv("CHUNK_SIZE", 1000))
        self.chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 200))
        self.top_k = int(os.getenv("TOP_K", 3))

        # DB
        self.chroma_db_path = os.getenv("CHROMA_DB_PATH", "./chroma_db")
        

# Crear una instancia de Settings para acceder a las configuraciones en toda la aplicación
settings = Settings()
