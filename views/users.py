from flask import request, abort
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from decorators import auth_required
from implemented import user_service

user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        email = user_service.get_email_by_token()
        user = user_service.get_by_email(email)
        user_d = UserSchema().dump(user)
        return user_d, 200

    @auth_required
    def patch(self):
        email = user_service.get_email_by_token()
        user = user_service.get_by_email(email)
        req_json = request.json
        req_json.id = user.id
        user_service.update(req_json)
        return "", 204


@user_ns.route('/password/')
class UserView(Resource):
    @auth_required
    def put(self):
        req_json = request.json
        old_password = req_json['old_password']
        new_password = req_json['new_password']
        if "Authorization" not in request.headers:
            abort(401)
        old_hash_password = user_service.get_old_hash_password()

        if user_service.compare_passwords(old_hash_password, old_password):
            email = user_service.get_email_by_token()
            user = user_service.get_by_email(email)
            user.password = user_service.get_hash(new_password)
            result = UserSchema().dump(user)
            try:
                user_service.update(result)
                return "пароль изменен", 204
            except Exception as e:
                return "пароль не изменен", e
