import jwt
from flask import request, abort

from constantans import JWT_SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        except Exception as e:
            print('decode error')
            abort(401)

        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])

            if user.get('role') != 'admin':
                abort(401)
        except Exception as e:
            print('decode error')
            abort(401)

        return func(*args, **kwargs)

    return wrapper
