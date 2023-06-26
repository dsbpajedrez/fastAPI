from fastapi import APIRouter
from utils.jwt_manager import create_token
from schemas.users import User
user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user : User):
    return create_token(user.dict())
