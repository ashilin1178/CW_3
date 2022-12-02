from typing import List, TypeVar

from flask import current_app
from flask_sqlalchemy import BaseQuery
from werkzeug.exceptions import NotFound

from dao.model.director import Director



class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        try:
            director_by_id = self.session.query(Director).get(bid)
            return director_by_id
        except Exception as e:
            return e

    def get_all(self) -> list:

        return self.session.query(Director)

    def create(self, director_d):
        ent = Director(**director_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        director = self.get_one(rid)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_d):
        director = self.get_one(director_d.get("id"))
        director.name = director_d.get("name")

        self.session.add(director)
        self.session.commit()
