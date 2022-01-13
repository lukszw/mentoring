"""
Application main file
Contain server app information
"""
from typing import Optional
import uvicorn
from fastapi import FastAPI
from db.config import engine, Base, async_session
from db.dals.dal import BookDAL
from db.models.book import Book

app = FastAPI()


@app.on_event("startup")
async def startup():
    """Creates DB table"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.post("/books", response_model=Book)
async def create_book(title: str, author: str, publication_year: int):
    """Function that creates new books"""
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.create_book(title, author, publication_year)


@app.put("/books/{book_id}")
async def update_book(
    book_id: int,
    title: Optional[str] = None,
    author: Optional[str] = None,
    publication_year: Optional[int] = None,
):
    """Function that updates exsisting books"""
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.update_book(book_id, title, author, publication_year)


@app.get("/books", response_model=Book)
async def get_books() -> list[Book]:
    """Function that returns all books in DB"""
    async with async_session() as session:
        async with session.begin():
            book_dal = BookDAL(session)
            return await book_dal.get_books()


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, host="127.0.0.1")
