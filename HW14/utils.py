import sqlite3


def db_connect(query, params, db='netflix.db'):
    with sqlite3.connect(db) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(query, params)

        result = cursor.fetchall()

    return result


def get_film_by_title(title):
    sql = "SELECT `show_id`,`title`,`type` from netflix where `title`=?"
    result = db_connect(sql, (title,))
    return [dict(row) for row in result]


def step_5(actor1, actor2):
    sql = f"SELECT `cast` FROM netflix WHERE `cast` LIKE ? AND `cast` LIKE ?"
    result = db_connect(sql, (f"%{actor1}%", f"%{actor2}%"))
    return [dict(row) for row in result]


def step_6(film_type, release_year, genre):
    sql = f"SELECT title, description FROM netflix WHERE type LIKE ? AND release_year = ? AND listed_in LIKE ?"
    result = db_connect(sql, (f'%{film_type}%', release_year, f'%{genre}%'))
    return [dict(row) for row in result]


if __name__ == '__main__':
    print(step_5('Rose McIver', 'Ben Lamb'))
