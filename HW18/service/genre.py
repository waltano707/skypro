class GenreService:

    def __init__(self, dao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, pk):
        return self.dao.get_one(pk)

    def create(self, data):
        return self.dao.create(data)

    def delete(self, pk):
        return self.dao.delete(pk)

    def update(self, pk, data):
        return self.dao.update(pk, data)
