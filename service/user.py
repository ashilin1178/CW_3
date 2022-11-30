import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_user_by_id(uid)

    def get_by_username(self, username):
        return self.dao.get_user_by_username(username)

    def get_all(self):
        return self.dao.get_all_users()

    def create(self, **user_data):
        user_data["password"] = self.get_hash(user_data["password"])
        return self.dao.create_user(**user_data)

    def update(self, uid, user_data):
        user_data["password"] = self.get_hash(user_data["password"])
        return self.dao.edit_user_by_id(uid, **user_data)

    def delete(self, uid):
        self.dao.delete_user_by_id(uid)

    def get_hash(self, password):
        """
        хэширование пароля пользователя
        :param password:
        :return:
        """
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        """
        проверка пароля пользователя
        :param password_hash:
        :param other_password:
        :return:
        """
        decoded_digest = base64.b64decode(password_hash)
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
