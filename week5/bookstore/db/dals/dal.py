"""
Data Access Layer
"""
from sqlalchemy import update
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from db.models.book import Book


class BookDAL:
    """Data Access Layer class for Add, Update and Get books"""

    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create_book(self, title: str, author: str, publication_year: int):
        """Function that creates a book and saves it in DB"""
        new_book = Book(title=title, author=author, publication_year=publication_year)
        self.db_session.add(new_book)
        await self.db_session.flush()

    async def get_books(self) -> list[Book]:
        """Function that return all books from DB"""
        q = await self.db_session.execute(select(Book))
        return q.scalars().all()

    async def update_book(
        self,
        book_id: int,
        title: str | None = None,
        author: str | None = None,
        publication_year: int | None = None,
    ):
        """Function that updates Book entitiy"""
        q = update(Book).where(Book.id == book_id)
        if title:
            q = q.values(title=title)
        if author:
            q = q.values(author=author)
        if publication_year:
            q = q.values(publication_year=publication_year)
        q.execution_options(synchronize_session="fetch")
        await self.db_session.execute(q)
