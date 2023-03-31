from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movie')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        filters = {}

        if request.args.get('director_id') != None:
            filters['director_id'] = request.args.get('director_id')

        filters = {}
        if director_id := request.args.get('director_id'):
            filters['director_id'] = director_id

        if genre_id := request.args.get('genre_id'):
            filters['genre_id'] = genre_id

        if year := request.args.get('year'):
            filters['year'] = year

        objs = movie_service.get_all(filters=filters)
        return MovieSchema(many=True).dump(objs), 200

    def post(self):
        try:
            MovieSchema().load(request.json)
        except ValueError:
            return "Неверные данные"

        obj = movie_service.create(request.json)
        return MovieSchema().dump(obj), 201, {'location': f'/movie/{obj.id}'}


@movie_ns.route('/<int:pk>')
class MovieView(Resource):
    def get(self, pk):
        obj = movie_service.get_one(pk)
        return MovieSchema().dump(obj), 200

    def delete(self, pk):
        movie_service.delete(pk)
        return "", 204

    def put(self, pk):
        obj = movie_service.update(pk, request.json)
        return MovieSchema().dump(obj), 200
