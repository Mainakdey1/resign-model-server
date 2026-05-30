from psycopg2 import OperationalError, InterfaceError
from psycopg2.extras import execute_values
from ..services.db_connection_service import get_connection, release_connection

def add_new_env_to_db(repository_name: str, envs: dict):

    conn =  get_connection()
    discard = False
    try:
        rows = [
            (repository_name, key, value)
            for key, value in envs.items()
        ]
        with conn.cursor() as cursor:

            execute_values(cursor, 
                           """
                            INSERT INTO test_envs (
                                project_name,
                                env_key,
                                env_value
                            )
                            VALUES %s
                            ON CONFLICT (project_name, env_key)
                            DO UPDATE SET
                                env_value = EXCLUDED.env_value;
                           """, rows)
        conn.commit()
        print('Environment variables recieved and stored successfully')
    except (OperationalError, InterfaceError):
        conn.rollback()
        discard = True
        raise
    finally:
        release_connection(conn, discard=discard)