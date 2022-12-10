from marshmallow import Schema, fields
from sqlalchemy import String, Integer

from setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    email = db.Column(String(100), unique=True, nullable=False)
    password = db.Column(String(255), nullable=False)
    name = db.Column(String(255))
    surname = db.Column(String(255))
    favorite_genre = db.Column(String(100))
    favorite_movies = db.Column(String(100))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
    favorite_movies = fields.Str()
