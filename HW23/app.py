import os
import re
from typing import Union, Iterable

from flask import Flask, request, Response
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


def slice_limit(it: Iterable, limit: int) -> Iterable:
    i = 0
    for element in it:
        if i < limit:
            yield element
        else:
            break
        i += 1


def apply_cmd(it: Iterable, cmd: str, value: str) -> Iterable:
    if cmd == 'filter':
        return filter(lambda x: value in x, it)
    if cmd == 'map':
        return map(lambda x: x.split(" ")[int(value)], it)
    if cmd == 'unique':
        return iter(set(it))
    if cmd == 'sort':
        return sorted(it, reverse=(value == 'desc'))
    if cmd == 'limit':
        return slice_limit(it, int(value))
    if cmd == 'reqex':
        reqex = re.compile(value)
        return filter(lambda x: reqex.search(x), it)

    return it


def build_query(it: Iterable, cmd1: str, value1: str, cmd2: str, value2:Union[str,int]) -> Iterable:
    it = apply_cmd(it, cmd1, value1)
    it = apply_cmd(it, cmd2, value2)
    return it


@app.post("/perform_query")
def perform_query() -> Response:
    try:
        file_name: str = request.form['file_name']

        cmd1: str = request.form['cmd1']
        value1: str = request.form['value1']
        cmd2: str = request.form['cmd2']
        value2: str = request.form['value2']


    except KeyError:
        raise BadRequest

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        raise BadRequest

    with open(file_path) as file:
        res = build_query(file, cmd1, value1, cmd2, value2)
        content = '\n'.join(res)

    return app.response_class(content, content_type="text/plain")


if __name__ == '__main__':
    app.run(port=5000, debug=True)
