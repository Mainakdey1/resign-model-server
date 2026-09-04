import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from fastapi import Depends

from src.services.database_query import get_env
from src.services.data_retrieval_hashenv import env_recieve
from src.core.config import settings
from src.services.add_new_env_to_db_service import add_new_env_to_db
from src.services.authentication.authentication_service import authenticate

class EnvData(BaseModel):
    repository_name: str
    envs: Dict[str, str]
app = FastAPI()

#Root endpoint
@app.get('/')
def root(
    authenticated: bool = Depends(authenticate)
):
    return {
        'message': settings.PROJECT_NAME,
        'version': settings.API_STR,
        'docs': '/docs',
        'status': 'operational',

    }
@app.get('/health')
def health(
    authenticated: bool=Depends(authenticate)
):
    return {'status': 'ok'}


@app.post('/base')
def base():
    return {'message': 'hello world'}

@app.post('/env-recieve')
def env_recieve(data: EnvData
             ):
    try:
        add_new_env_to_db(data.repository_name, data.envs)
        return {'message': 'Environment variables recieved and stored successfully'}
    except Exception as e:
        return {'message': f'An error occurred: {str(e)}'}



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
