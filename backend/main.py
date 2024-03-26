import json
from fastapi import FastAPI
from PyMovieDb import IMDB
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

imdb = IMDB()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get('/movies')
async def popular_movies():
    popular_movies = imdb.popular_movies()
    print(popular_movies)
    return json.loads(popular_movies)
    
@app.get("/movie/{filme_name}")
async def movie_detail(filme_name: str):
    film = imdb.get_by_name(filme_name)
    return json.loads(film)

