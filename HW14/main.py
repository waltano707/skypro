from flask import Flask, jsonify
import sqlite3

from HW14.utils import get_film_by_title

app = Flask(__name__)


def db_connect(query, params, db='netflix.db'):
    with sqlite3.connect(db) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()

    return result


@app.route("/movie/<title>/")
def search_film_by_title(title):
    return jsonify(get_film_by_title(title))


@app.route("/movie/<int:from_year>/to/<int:to_year>/")
def search_film_by_year(from_year, to_year):
    sql = "SELECT `show_id`,`title`,`type`,`release_year` from netflix where `release_year` between ? and ?"
    result = db_connect(sql, (from_year, to_year,))
    result = [dict(row) for row in result]
    return jsonify(result)


@app.route("/rating/<rating>/")
def search_film_by_rating(rating):
    if rating == 'children':
        sql = "SELECT `show_id`,`title`,`type`,`rating` from netflix where `rating` in ('G')"
    elif rating == 'family':
        sql = "SELECT `show_id`,`title`,`type`,`rating` from netflix where `rating` in ('G','PG','PG-13')"
    elif rating == 'adult':
        sql = "SELECT `show_id`,`title`,`type`,`rating` from netflix where `rating` in ('R','NC-17')"
    else:
        return ''

    result = db_connect(sql, tuple())
    result = [dict(row) for row in result]
    return jsonify(result)


@app.route("/genre/<genre>/")
def search_film_by_genre(genre):
    sql = f"SELECT `show_id`,`title`,`type`,`release_year`,`listed_in` from netflix where `listed_in` like ? order by `release_year` desc"
    result = db_connect(sql, (f'%{genre}%',))
    result = [dict(row) for row in result][:10]
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
