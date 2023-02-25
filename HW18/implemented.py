from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService
from setup_db import db

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)
