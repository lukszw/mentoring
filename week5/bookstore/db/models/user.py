"""
User model file, create table and metadata
"""
from sqlalchemy import Column, Integer, String
from db.config import Base


class User(Base):
    """
    Class containing information about
    table where and how users will be stored
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)


    def __repr__(self) -> str:
        return f"<User=(username={self.username}, password={self.password}, email={self.email})>)"