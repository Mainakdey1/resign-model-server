from psycopg2.pool import SimpleConnectionPool
from psycopg2 import OperationalError, InterfaceError


from src.core.config import settings

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=50,
    dsn=settings.DATABASE_URL
)

def get_connection():

    conn = pool.getconn()

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")

        return conn

    except (OperationalError, InterfaceError):

        pool.putconn(conn, close=True)
        conn = pool.getconn()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")

        return conn

def release_connection(conn, discard=False):
    pool.putconn(conn, close=discard)


def close_all_connections():
    pool.closeall()

