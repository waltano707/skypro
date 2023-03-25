from dao.base_dao import BaseDAO
from dao.models.genre import Genre


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre
