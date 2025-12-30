from contextlib import contextmanager
import mysql.connector
from mysql.connector import MySQLConnection

from wellness_tracker.core.config import DBConfig


@contextmanager
def connect(db: DBConfig) -> MySQLConnection:
    con = mysql.connector.connect(
        host=db.host,
        user=db.user,
        password=db.password,
        database=db.database,
        port=db.port,
    )
    try:
        yield con
    finally:
        con.close()
