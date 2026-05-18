#fetches data from DB. Prepares data to be packaged in json and sent to client cli.
import os
from ..core.config import settings

def env_recieve(repository_name):
    ENV_STORE = settings.ENV_STORE

    path = os.path.join(ENV_STORE, f"{repository_name}")
    if not os.path.exists(path):
        return ("Env file not found")
        

    env_data = {}

    with open(path, "r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = line.split("=", 1)

            env_data[key] = value


    return env_data

    