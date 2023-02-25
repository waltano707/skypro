from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, pk):
        return self.session.query(Movie).get(pk)

    def delete(self, pk):
        obj = self.get_one(pk)
        self.session.delete(obj)
        self.session.commit()

    def update(self, pk, data):
        obj = self.get_one(pk)

        obj.title = data.get('title')
        obj.description = data.get('description')
        obj.trailer = data.get('trailer')
        obj.year = data.get('year')
        obj.rating = data.get('rating')

        self.session.add(obj)
        self.session.commit()

        return obj

    def get_all(self, filters=None):
        query = self.session.query(Movie)
        query = self.filter_query(query, filters) if filters else query
        return query.all()

    def filter_query(self, query, filters):
        if director_id := filters.get('director_id'):
            query = query.filter(Movie.director_id == director_id)

        if genre_id := filters.get('genre_id'):
            query = query.filter(Movie.genre_id == genre_id)

        if year := filters.get('year'):
            query = query.filter(Movie.year == year)
        return query

    def create(self, data):
        obj = Movie(**data)
        self.session.add(obj)
        self.session.commit()

        return obj
