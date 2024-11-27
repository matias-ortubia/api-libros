from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    price: float = None
    is_available: bool = True

