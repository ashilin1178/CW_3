from marshmallow import Schema, fields
from sqlalchemy import ForeignKey, Integer, String, Float

from setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    title = db.Column(String(100), nullable=False)
    description = db.Column(String(255), nullable=False)
    trailer = db.Column(String(255), nullable=False)
    year = db.Column(Integer, nullable=False)
    rating = db.Column(Float, nullable=False)
    genre_id = db.Column(Integer, ForeignKey("genre.id"), nullable=False)
    genre = db.relationship("Genre")
    director_id = db.Column(Integer, ForeignKey("director.id"), nullable=False)
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()
