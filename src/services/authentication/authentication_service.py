from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def authenticate(
        credentials: HTTPAuthorizationCredentials = Depends(security)
):

    

    token = credentials.credentials
    if not token:
        raise HTTPException(
            status_code=401,
            detail='Missing token'
        )
    if token == 'secret-token':
        return True
    else:
        raise HTTPException(
            status_code=401,
            detail='Invalid token'
        )