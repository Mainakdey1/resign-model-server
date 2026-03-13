import uvicorn
from fastapi import FastAPI
import os
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

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", 
                    host=settings.HOST, 
                    port=settings.PORT, 
                    reload=settings.DEBUG)
    except(KeyboardInterrupt, SystemExit):
        print('System stopped by user')
