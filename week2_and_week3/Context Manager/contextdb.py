import sqlalchemy
import pandas as pd
from typing import Generator
from sqlalchemy import create_engine, exc
from contextlib import contextmanager


@contextmanager
def get_db(
        username: str,
        password: str,
        host: str,
        port: str,
        db: str
) -> Generator[sqlalchemy.engine.base.Engine, None, None]:
    """
    Context manager to manage our DB connection.
    Variables:
    - username: Username
    - password: Password
    - host: host name of the database
    - port: port of the database
    - db: database name
    """
    conn_str = f"oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={db}"
    conn = create_engine(conn_str)

    try:
        print("Connecting...")
        yield conn

    except exc.SQLAlchemyError as err:
        print(f"Error occured {err}")

    finally:
        print("Pulling data completed ... dispose connection")
        conn.dispose()


with get_db("username", "password", "hostname", "1234", "dbname") as conn:
    data = pd.read_sql("SELECT * FROM dual", conn)

print(data.head())
