from marshmallow import Schema, fields
from sqlalchemy import Integer, String

from setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()

