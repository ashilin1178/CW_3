from flask import request
from flask_restx import Namespace, Resource
from implemented import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class AuthsView(Resource):
    def post(self):
        req_json = request.json
        try:
            user_service.create(**req_json)
        except Exception as e:
            return e, 400
        return "User created", 201, {"location": f"/users/"}

@auth_ns.route('/login/')
class AuthsView(Resource):

    def post(self):
        """
        первоначальная аутентификация
        :return:
        """
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            return "введите email и пароль", 400
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):

        try:
            data = request.json
            token = data.get("refresh_token")

            tokens = auth_service.approve_refresh_token(token)

            return tokens, 201
        except Exception as e:
            return str(e), 401
