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



def get_env(repository_name: str):

    conn =  get_connection()
    discard = False

    if conn.closed:
        pool.putconn(conn, close=True)
        conn = pool.getconn()
    try:
        try: 
            with conn.cursor() as cursor:
                cursor.execute("SELECT 1")
        except (OperationalError, InterfaceError):
            discard = True
            raise
        with conn.cursor() as cursor:

            cursor.execute("""
                SELECT env_key, env_value
                FROM test_envs
                WHERE project_name = %s
            """, (repository_name,))

            rows = cursor.fetchall()

            envs = {}

            for key, value in rows:
                envs[key] = value

            return envs
    except (OperationalError, InterfaceError):
        discard = True
        raise
    finally:
        pool.putconn(conn, close=discard)