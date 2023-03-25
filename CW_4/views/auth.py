import jwt
from flask import request
from flask_restx import Resource, Namespace

from constants import JWT_SECRET_KEY, JWT_TOKEN_ALGORITHM
from container import user_service
from utils import generate_jwt, get_hash, is_email_valid

auth_ns = Namespace('auth')


@auth_ns.route('/login/')
class AuthView(Resource):
    # Аутентификация по логину/паролю и выдача токенов
    @auth_ns.doc(params={
        'email': {'description': 'Электронная почта', 'in': 'formData', 'example': 'test@email.ru'},
        'password': {'description': 'Пароль', 'in': 'formData', 'example': 'admin'},
    })
    def post(self):
        """
        Аутентификация по email и паролю.
        В параметрах запроса ожидаем:
            email: str
            password: str
            :return: {'access_token': access_token, 'refresh_token': refresh_token}
        """
        req_json = request.json
        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in [email, password]:
            return {"error": "Неверные учётные данные"}, 400

        user = user_service.get_by_email(email)

        # Проверяем существует ли вообще такой пользователь
        if user is None:
            return {"error": "Неверные учётные данные"}, 401
        # И, верный ли введён пароль
        if user.password != get_hash(password):
            return {"error": "Неверные учётные данные"}, 401

        user_data = {"email": user.email,
                     "id": user.id,
                     }

        tokens = generate_jwt(user_data)
        return tokens, 201

    # Аутентификация по рефреш токену и обновление access токена
    @auth_ns.doc(params={
        'email': {'description': 'Электронная почта', 'in': 'formData', 'example': 'test@email.ru'},
        'refresh_token': {'description': 'Токен для обновления аутентификации', 'in': 'formData'},
    })
    def put(self):
        """
        В функции обновляем токены доступа по рефреш токену.
        В данных запроса ожидаем увидеть:
            email: str
            refresh_token: str
            :return: {'access_token': access_token, 'refresh_token': refresh_token}
        """

        user_refresh_token_data = request.json()
        refresh_token = user_refresh_token_data.get('refresh_token')

        if refresh_token is None:
            return {"error": "Неверные учётные данные"}, 400

        try:
            decoded_token = jwt.decode(
                refresh_token, JWT_SECRET_KEY, algorithms=[JWT_TOKEN_ALGORITHM])
        except Exception:
            return {"error": "Неверные учётные данные"}, 401

        # Если имя в данных токена не соответствует имени в запросе
        if decoded_token.get('email') != user_refresh_token_data.get('email'):
            return {"error": "Неверные учётные данные"}, 401

        user_data = {'email': decoded_token.get('email'),
                     'id': decoded_token.get('id'),
                     }

        new_tokens = generate_jwt(user_data)
        return new_tokens, 201


@auth_ns.route('/register/')
class NewUserRegister(Resource):
    @auth_ns.header('Content-Type', 'application/json')
    @auth_ns.doc(params={
        'email': {'description': 'Электронная почта', 'in': 'formData', 'example': 'test@email.ru'},
        'password': {'description': 'Пароль', 'in': 'formData', 'example': 'admin'},
    })
    def post(self):
        """
        Регистрирует нового пользователя в системе.
        В качестве параметров запроса обязательно
        ждём электронную почту и пароль
        :return: "", 201
        """
        req_json = request.data or request.json

        email = req_json.get("email", None)
        password = req_json.get("password", None)
        if None in [email, password]:
            return {"error": "Неверные учётные данные"}, 400

        # Проверяем, что такого пользователя еще нет
        if user_service.get_by_email(email):
            return {"error": "Такой пользователь уже существует"}, 400

        # Проверяем валидность электронной почты
        if not is_email_valid(email):
            return {"error": "В качестве имени пользователя указан не корректные email"}, 400

        # Не знаю, стоит ли тут вернуть сразу токены авторизации?
        user = user_service.create(req_json)
        return "", 201, {'localtion': f'/users/{user.id}'}
