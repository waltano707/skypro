from dao.base_dao import BaseDAO
from dao.models.director import Director


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director

