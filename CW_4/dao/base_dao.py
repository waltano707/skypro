from typing import TypeVar, Generic

from flask import current_app
from sqlalchemy.orm import Query
from sqlalchemy.orm import scoped_session

from dao.models.basemodel import BaseModel

T = TypeVar('T', bound=BaseModel)


class BaseDAO(Generic[T]):
    __model__ = T

    def __init__(self, session: scoped_session):
        self.session = session

    @property
    def _items_per_page(self) -> int:
        return current_app.config['ITEMS_PER_PAGE']

    def get_one(self, uid: int) -> T | None:
        return self.session.get(self.__model__, uid)

    def get_all(self, page: int | None = None) -> list[T]:
        stmt: Query = self.session.query(self.__model__)
        if page:
            try:
                # return stmt.paginate(page=1, max_per_page=2).items
                return stmt.paginate(page=page,
                                     per_page=self._items_per_page).items
            except Exception:
                return []
        return stmt.all()

    def create(self, entity_data: dict) -> T:
        entity = self.__model__(**entity_data)
        self.session.add(entity)
        self.session.commit()
        return entity

    def update(self, entity: T) -> T:
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, uid) -> T:
        entity = self.get_one(uid)

        self.session.delete(entity)
        self.session.commit()
        return entity
