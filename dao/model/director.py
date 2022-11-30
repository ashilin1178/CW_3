from marshmallow import Schema, fields
from sqlalchemy import Integer, String, DateTime, func

from setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(Integer, primary_key=True, autoincrement=True)
    name = db.Column(String(100), unique=True, nullable=False)
    created = db.Column(DateTime, nullable=False, default=func.now())
    updated = db.Column(DateTime, default=func.now(), onupdate=func.now())


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
