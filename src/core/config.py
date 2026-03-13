from pydantic import Field, field_validator
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):

    API_STR: str = 'api/v1'
    PROJECT_NAME: str = 'ReSign Model Server'

    HOST:str = Field(os.getenv('HOST'))
    PORT:int = Field(os.getenv('PORT'))

    DEBUG:bool = Field(default=True, env='DEBUG')

settings = Settings()