import uvicorn
from fastapi import FastAPI

from src.services.database_query import get_env
from src.services.data_retrieval_hashenv import env_recieve
from src.core.config import settings
app = FastAPI()

#Root endpoint
@app.get('/')
def root():
    return {
        'message': settings.PROJECT_NAME,
        'version': settings.API_STR,
        'docs': '/docs',
        'status': 'operational',

    }
@app.get('/health')
def health():
    return {'status': 'ok'}

@app.post('/base')
def base():
    return {'message': 'hello world'}

@app.get("/sum")
def calculate_sum(a: int, b: int):
    return {
        "sum": a + b
    }

@app.get('/env/{repository_name}')
def get_env_endpoint(repository_name: str):
    env_data = get_env(repository_name)
    return env_data

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", 
                    host=settings.HOST, 
                    port=settings.PORT, 
                    reload=settings.DEBUG)
    except(KeyboardInterrupt, SystemExit):
        print('System stopped by user')
