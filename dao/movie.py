from sqlalchemy import desc

from constants import LIMIT_VALUE, OFFSET_VALUE
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self, filters: dict) -> list:
        movies_query = self.session.query(Movie)
        if filters['director_id'] is not None:
            movies_query = movies_query.filter(Movie.director_id == filters['director_id'])
        if filters['genre_id'] is not None:
            movies_query = movies_query.filter(Movie.genre_id == filters['genre_id'])
        if filters['year'] is not None:
            movies_query = movies_query.filter(Movie.year == filters['year'])
        if filters['status'] is not None and filters['status'] == 'new':
            movies_query = movies_query.order_by(desc(Movie.id))
        else:
            movies_query = movies_query.offset(OFFSET_VALUE * (int(filters['page']) - 1)).limit(LIMIT_VALUE)

        return movies_query.all()

    def create(self, **movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        movie = self.get_one(rid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        try:
            movie = self.session.query(Movie).filter(Movie.id == movie_d.id).update(movie_d)
            self.session.add(movie)
            self.session.commit()
        except Exception as e:
            return e
