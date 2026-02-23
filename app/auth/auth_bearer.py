from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from .auth_handler import SECRET_KEY, ALGORITHM

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)

        if credentials:
            token = credentials.credentials
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                return payload
            except:
                raise HTTPException(status_code=403, detail="Token inválido")
        else:
            raise HTTPException(status_code=403, detail="Token no encontrado")