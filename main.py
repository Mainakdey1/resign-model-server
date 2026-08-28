import uvicorn
from importlib import import_module
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

from src.services.database_query import get_env
from src.services.data_retrieval_hashenv import env_recieve
from src.core.config import settings
from src.services.add_new_env_to_db_service import add_new_env_to_db
from src.services.retrieve_mail_service import get_gmail_data

class EnvData(BaseModel):
    repository_name: str
    envs: Dict[str, str]
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


@app.get('/mail/list')
def get_mail_list():
    res, top_message = get_gmail_data()
    print(res)
    return top_message

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", 
                    host=settings.HOST, 
                    port=settings.PORT, 
                    reload=settings.DEBUG)
    except(KeyboardInterrupt, SystemExit):
        print('System stopped by user')
