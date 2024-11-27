from fastapi import APIRouter, HTTPException
from app.models.book_model import Book

router = APIRouter()
books_db = {}


@router.get("/books", summary = "Obtener todos los libros")
def get_books():
    return {"books": list(books_db.values())}

@router.get("/books/{book_id}", summary = "Obtener un libro por ID")
def get_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code = 404, detail = "Libro no encontrado")
    return books_db[book_id]

@router.post("/books", summary = "Agregar un nuevo libro")
def create_book(book: Book):
    if book.id in books_db:
        raise HTTPException(status_code = 400, detail = "El ID ya existe")
    books_db[book.id] = book.dict()
    return {"message": "Libro creado", "book": book}

@router.put("/books/{book_id}", summary = "Actualizar un libro existente")
def update_book(book_id: int, book: Book):
    if book_id not in books_db:
        raise HTTPException(status_code = 404, detail = "Libro no encontrado")
    books_db[book_id] = book.dict()
    return {"message": "Libro actualizado", "book": Book}

@router.delete("/books/{book_id}", summary = "Eliminar un libro")
def delete_book(book_id: int):
    if book_id not in books_db:
        raise HTTPException(status_code = 404, detail = "Libro no encontrado")
    del books_db[book_id]
    return {"message": "Libro eliminado"}

