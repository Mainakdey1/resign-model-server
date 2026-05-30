from psycopg2 import OperationalError, InterfaceError
from ..services.db_connection_service import get_connection, release_connection

def get_env(repository_name: str):
    discard = False
    conn =  get_connection()
    try:
        with conn.cursor() as cursor:

            cursor.execute("""
                SELECT env_key, env_value
                FROM test_envs
                WHERE project_name = %s
            """, (repository_name,))

            rows = cursor.fetchall()

            return {
                key: value
                for key, value in rows
            }
    except (OperationalError, InterfaceError):
        discard = True
        raise
    finally:
        release_connection(conn, discard=discard)