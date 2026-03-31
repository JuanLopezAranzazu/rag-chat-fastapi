from fastapi import APIRouter, UploadFile, File
import shutil
from rag.loader import load_and_split
from rag.embeddings import save_to_db
from rag.chain import ask_question

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Recibe un archivo PDF, lo procesa y guarda su contenido en la base de datos."""
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = load_and_split(file_path)
    save_to_db(chunks)

    return {"message": "Documento procesado correctamente"}


@router.post("/ask")
async def ask(query: str):
    """Recibe una pregunta, la procesa utilizando un modelo generativo y devuelve la respuesta."""
    response = ask_question(query)
    return {"response": response}
