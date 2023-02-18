# app.py

from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

api = Api(app)
movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int(validate=validate.Range(min=1900, max=2030))
    rating = fields.Float()


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = Movie.query

        if genre_id := request.args.get('genre_id'):
            movies = movies.filter(Movie.genre_id == genre_id)

        if director_id := request.args.get('director_id'):
            movies = movies.filter(Movie.director_id == director_id)

        return movies_schema.dump(movies.all()), 200

    def post(self):
        req = request.json
        try:
            movie_schema.load(request.json)
        except  ValidationError as e:
            return str(e), 500

        new_movie = Movie(**req)
        with db.session.begin():
            db.session.add(new_movie)

        return movie_schema.dump(new_movie), 201, {'location': f'/movies/{new_movie.id}'}


@movies_ns.route('/<int:pk>')
class MovieView(Resource):
    def get(self, pk):

        movie = Movie.query.get(pk)
        return movie_schema.dump(movie), 200

    def delete(self, pk):
        movie = Movie.query.get(pk)
        with db.session.begin():
            db.session.delete(movie)
        return '', 204

    def patch(self, pk):
        movie = Movie.query.get(pk)
        req = request.json

        if title := req.get('title'):
            movie.title = title

        if description := req.get('description'):
            movie.description = description

        if trailer := req.get('trailer'):
            movie.trailer = trailer

        if year := req.get('year'):
            movie.year = year

        if rating := req.get('rating'):
            movie.rating = rating

        db.session.add(movie)
        db.session.commit()
        return movie_schema.dump(movie), 200, {'location': f'/movies/{movie.id}'}

    def put(self, pk):
        movie = Movie.query.get(pk)
        req = request.json

        movie.title = req.get('title')
        movie.description = req.get('description')
        movie.trailer = req.get('trailer')
        movie.year = req.get('year')
        movie.rating = req.get('rating')

        db.session.add(movie)
        db.session.commit()
        return movie_schema.dump(movie), 200, {'location': f'/movies/{movie.id}'}


@app.route('/main/', strict_slashes=False)
def main():
    return 'main'


if __name__ == '__main__':
    app.run(debug=True)
