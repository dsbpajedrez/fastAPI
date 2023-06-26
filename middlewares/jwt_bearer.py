from fastapi import  HTTPException
from fastapi.security import HTTPBearer
from starlette.requests import Request
from utils.jwt_manager import  validate_token

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email']!= "david":
            raise HTTPException(status_code=403, detail="Credenciales inválidas")
    