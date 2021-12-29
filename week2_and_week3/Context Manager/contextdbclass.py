import pandas as pd
import sqlalchemy
from typing import Optional, Type
from types import TracebackType
from sqlalchemy import create_engine, exc


class DBConnection:
    """
    DBConnection class works as context manager to mange DB connection

    Variable:
    - username: username
    - password: password
    - host: host name of the database
    - port: port of the database
    - db: database name
    """
    def __init__(self, username: str, password: str, host: str, port: str, db: str) -> None:
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db = db

    def __enter__(self) -> sqlalchemy.engine.base.Engine:
        conn_str = f"oracle+cx_oracle://{self.username}:{self.password}@{self.host}:{self.port}/?service_name={self.db}"
        self.conn = create_engine(conn_str)
        return self.conn

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        exc_tb: Optional[TracebackType]
    ) -> Optional[bool]:
        ...
        if isinstance(exc_value, exc.SQLAlchemyError):
            print(f"Error occured {exc_type} -> {exc_value} -> {exc_tb}")
            return True
        else:
            print("Pulling data completed ... dispose connection")
            self.conn.dispose()
            return False


with DBConnection("username", "password", "hostname", "port", "db") as conn:
    print("Connecting...")
    data = pd.read_sql("SELECT * FROM dual", conn)


print(data.head())
