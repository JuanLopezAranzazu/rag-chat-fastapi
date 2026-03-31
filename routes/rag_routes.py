from fastapi import APIRouter, UploadFile, File
import shutil
from rag.loader import load_and_split
from rag.embeddings import save_to_db
from rag.chain import ask_question

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Recibe un archivo PDF, lo procesa y guarda su contenido en la base de datos."""
    # Guardar el archivo temporalmente para su procesamiento
    file_path = f"temp_{file.filename}"
    # Guardar el archivo subido en el sistema de archivos local
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # Cargar el archivo, dividirlo en fragmentos y guardar los fragmentos en la base de datos
    chunks = load_and_split(file_path)
    # Guardar los fragmentos de texto en la base de datos utilizando la función save_to_db
    save_to_db(chunks)

    return {"message": "Documento procesado correctamente"}


@router.post("/ask")
async def ask(query: str):
    """Recibe una pregunta, la procesa utilizando un modelo generativo y devuelve la respuesta."""
    # Responder a la pregunta utilizando la función ask_question y devolver la respuesta en formato JSON
    response = ask_question(query)
    return {"response": response}
