from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token

app = FastAPI()

app.title = "Mi primer api en fastAPI"
app.version = "0.0.1"


class User(BaseModel):
    email : str
    password : str
class Movie(BaseModel):
    id: Optional[int] | None = None
    title: str = Field(min_length=5, max_length=50)
    overview: str = Field(min_length=5, max_length=50)
    year: int = Field(le= 2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=50)
    class Config:
        schema_extra= {
            "example": {
                "id" : 1,
                "title" : "Titulo de mi película",
                "overview": "Descripción de mi película",
                "year": 2023,
                "rating": 10,
                "category": "Categoría de mi película"
            }
        }

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

@app.post('/login', tags=['auth'])
def login(user : User):
    print(user)
    return create_token(user.dict())


@app.get('/movies',tags=['movie'])
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get('/movie/{id}' ,tags=['movie'], response_model=Movie)
def get_movie_by_id(id : int=Path(ge=1, le=1000))->dict:
    movie = list(filter(lambda item : item['id']==id,movies))
    if movie == []:
        return JSONResponse(content=[], status_code=404)
    return JSONResponse(status_code=200, content=movie)


@app.get('/movies/', tags=['movie'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=20))-> List[Movie]:
    movie = list(filter(lambda item: item['category']== category, movies))
    return JSONResponse(status_code=200, content=movie)

@app.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie)-> dict:
    movies.append(movie.dict())
    return JSONResponse(status_code=201, content={"message": "Registro exitoso"})

@app.put('/movies/{id}', tags=['movie'], response_model=dict, status_code=200)
def upadte_movie( movie: Movie,id: int= Path(le=1000, ge=1))-> dict:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(status_code=200,content={"message":"Modificación exitoso"})
        
@app.delete('/movie/{id}', tags=['movie'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    for movie in movies:
        if movie['id'] == id:
            index = movies.index(movie)
            movies.pop(index)
            #una manera mas simlificada es :
            # movies.remove(movie) sin tener que buscar el index
            return JSONResponse(status_code=200, content={"message": "Elimanda de manera exitosa"})


