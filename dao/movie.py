from sqlalchemy import desc

from constants import LIMIT_VALUE, OFFSET_VALUE
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Movie).get(bid)

    def get_all(self, director_id=None, genre_id=None, year=None, page=None, status=None) -> list:
        movies_query = self.session.query(Movie)
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)
        if year is not None:
            movies_query = movies_query.filter(Movie.year == year)
        if status is not None and status == 'new':
            movies_query = movies_query.order_by(desc(Movie.id))
        else:
            if page is not None and int(page) > 0:
                movies_query = movies_query.limit(LIMIT_VALUE).offset(OFFSET_VALUE * (int(page) - 1))

        return movies_query.all()

    def create(self, movie_d):
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
