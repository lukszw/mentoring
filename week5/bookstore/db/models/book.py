"""
Book model file, create table and metadata
"""
from sqlalchemy import Column, Integer, String
from db.config import Base


class Book(Base):
    """
    Class containing information about
    table where and how books will be stored
    """

    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"<Book=(title={self.title}, author={self.author}, publication_year={self.publication_year})>)"
