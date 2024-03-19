from PyMovieDb import IMDB

imdb = IMDB()
res = imdb.get_by_name('Dune', tv=False)

print(res)
