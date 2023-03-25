from dao.models.director import DirectorSchema
from dao.models.favorite import FavoriteSchema
from dao.models.genre import GenreSchema
from dao.models.movie import MovieSchema
from dao.models.user import UserSchema

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO
from dao.user import UserDAO
from dao.favorite import FavoritesDAO

from services.director import DirectorService
from services.favorite import FavoritesService
from services.genre import GenreService
from services.movie import MovieService
from services.user import UserService

from setup.db import db

genre_dao = GenreDAO(db.session)
director_dao = DirectorDAO(db.session)
movie_dao = MovieDAO(db.session)
user_dao = UserDAO(db.session)
favorites_dao = FavoritesDAO(db.session)

genre_service = GenreService(genre_dao)
director_service = DirectorService(director_dao)
movie_service = MovieService(movie_dao)
user_service = UserService(user_dao)
favorites_service = FavoritesService(favorites_dao)

genre_schema = GenreSchema()
director_schema = DirectorSchema()
movie_schema = MovieSchema()
user_schema = UserSchema()
favorites_schema = FavoriteSchema
