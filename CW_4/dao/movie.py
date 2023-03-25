from sqlalchemy.orm import Query

from dao.base_dao import BaseDAO
from dao.models.movie import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all(self,
                page: int | None = None,
                novelties: bool = False) -> list[Movie]:

        stmt: Query = self.session.query(self.__model__)
        if novelties:
            stmt = stmt.order_by(self.__model__.year.desc())

        if page:
            try:
                # return stmt.paginate(page=1, max_per_page=2).items
                return stmt.paginate(page=page, per_page=ITEMS_PER_PAGE).items
            except Exception:
                return []

        return stmt.all()
