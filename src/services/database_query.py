from fastapi import FastAPI
from dotenv import load_dotenv
import psycopg2

from src.core.config import settings

load_dotenv()

DATABASE_URL = settings.DATABASE_URL
print(DATABASE_URL)

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

app = FastAPI()

def get_env(repository_name: str):
    cursor.execute("""
    SELECT current_database();
    """)

    print(cursor.fetchall())
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