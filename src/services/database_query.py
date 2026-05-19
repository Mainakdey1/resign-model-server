from psycopg2.pool import SimpleConnectionPool
from src.core.config import settings

pool = SimpleConnectionPool(
    minconn=1,
    maxconn=50,
    dsn=settings.DATABASE_URL
)

def get_env(repository_name: str):

    conn = pool.getconn()

    try:
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

    finally:
        pool.putconn(conn)