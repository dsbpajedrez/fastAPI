from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse
from typing import List
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from config.database import session
from service.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()


@movie_router.get('/movies',tags=['movie'], dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movie/{id}' ,tags=['movie'], response_model=Movie)
def get_movie_by_id(id : int=Path(ge=1, le=1000))->dict:
    db = session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'not found'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get('/movies/', tags=['movie'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=50))-> List[Movie]:
    db = session()
    result = MovieService(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message':'Not found!'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.post('/movies', tags=['Movies'], response_model=dict, status_code=201)
def create_movie(movie: Movie)-> dict:
    db = session()
    MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={"message": "Registro exitoso"})

@movie_router.put('/movies/{id}', tags=['movie'], response_model=dict, status_code=200)
def upadte_movie( movie: Movie,id: int= Path(le=1000, ge=1))-> dict:
    db = session()
    movie_to_update = MovieService(db).get_movie_by_id(id)
    if not movie_to_update:
            return JSONResponse(status_code=404, content={'message':'not found'})
    MovieService(db).update_movie(movie,movie_to_update)
    return JSONResponse(status_code=200,content={"message":"Modificación exitoso"})
        
@movie_router.delete('/movie/{id}', tags=['movie'], response_model=dict, status_code=200)
def delete_movie(id: int)-> dict:
    db = session()
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'not found man!'})
    MovieService(db).delete_movie(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Elimanda de manera exitosa"})


