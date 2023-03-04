from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json

        username = req_json.get('username')
        password = req_json.get('password')

        if None in [username, password]:
            return '', 400

        tokens = auth_service.generate_tokens(username, password)

        return tokens, 201
