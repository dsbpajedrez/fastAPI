from fastapi import FastAPI
from pydantic import BaseModel
from jwt_manager import create_token

app = FastAPI()

movies = [
    {
        "id":1,
        "title":"Mi primer película",
        "overview":"Mi primer overview",
        "year":2021,
        "rating":3.4,
        "category":"Acción"
    },
        {
        "id":2,
        "title":"Mi segunda película",
        "overview":"Mi segunda overview",
        "year":2022,
        "rating":9.0,
        "category":"Ciencia ficción"
    }
]

class User(BaseModel):
    email : str
    password : str

@app.post('/login', tags=['auth'])
def login(user : User):
    print(user)
    return create_token(user.dict())


@app.get('/movies',tags=['movie'])
def get_movies():
    return movies

@app.get('/movie/{id}')
def get_movie_by_id(id : int):
    movie = list(filter(lambda item : item['id']==id,movies))
    return movie