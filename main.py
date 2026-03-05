import uvicorn
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
@app.post("/base")
def base():
    return {'message': 'hello world'}

if __name__ == "__main__":
    port = int(os.getenv('PORT'))
    host = os.getenv('HOST')
    uvicorn.run(app, host=host, port=port)