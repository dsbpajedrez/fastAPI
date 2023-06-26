from fastapi import FastAPI
from config.database import session, engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()

app.title = "Mi primer api en fastAPI"
app.version = "0.0.1"
app.add_middleware(ErrorHandler) # Añade el middleware a nivelo global de la apliación
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


