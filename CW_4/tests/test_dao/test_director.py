import pytest

from dao.director import DirectorDAO
from dao.models.director import Director


class TestDirectorsDAO:

    @pytest.fixture
    def directors_dao(self, db):
        return DirectorDAO(db.session)

    @pytest.fixture
    def director_1(self, db):
        g = Director(name="Кустурица")
        db.session.add(g)
        db.session.commit()
        return g

    @pytest.fixture
    def director_2(self, db):
        g = Director(name="Тарантино")
        db.session.add(g)
        db.session.commit()
        return g

    def test_get_director_by_id(self, director_1, directors_dao):
        assert directors_dao.get_one(director_1.id) == director_1

    def test_get_director_by_id_not_found(self, directors_dao):
        assert not directors_dao.get_one(1)

    def test_get_all_directors(self, directors_dao, director_1, director_2):
        assert directors_dao.get_all() == [director_1, director_2]

    def test_get_directors_by_page(self, app, directors_dao, director_1, director_2):
        app.config['ITEMS_PER_PAGE'] = 1
        assert directors_dao.get_all(page=1) == [director_1]
        assert directors_dao.get_all(page=2) == [director_2]
        assert directors_dao.get_all(page=3) == []
