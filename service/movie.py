from fastapi.responses import JSONResponse
from models.movie import Movie as MovieModel
from schemas.movie import Movie
class MovieService():
    def __init__(self, db) -> None:
        self.db = db    

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie_by_id(self, id):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result
    
    def get_movie_by_category(self, category):
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result
    
    def create_movie(self, movie: Movie):
        result = MovieModel(**movie.dict())
        self.db.add(result)
        self.db.commit()
        return 
    
    def update_movie(self,  movie_updated:Movie, movie:Movie):       
        movie.title = movie_updated.title
        movie.overview = movie_updated.overview
        movie.year = movie_updated.year
        movie.rating = movie_updated.rating
        movie.category = movie_updated.category
        self.db.commit()
        return
    
    def delete_movie(self, movie:Movie):
        self.db.delete(movie)
        self.db.commit()
        return 

