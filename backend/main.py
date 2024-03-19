from fastapi import FastAPI
from PyMovieDb import IMDB
import json

app = FastAPI()

imdb = IMDB()

@app.get('/')
async def popular_movies():
    popular_movies = imdb.popular_movies()
    return json.loads(popular_movies)

@app.get("/movie/{filme_name}")
async def movie_detail(filme_name: str):
    film = imdb.get_by_name(filme_name)
    return json.loads(film)

