from models import Film
from ast import literal_eval


class FilmRepository:
    """ Film repository for Film model """

    @staticmethod
    def get_all():
        return Film.query.all()

    @staticmethod
    def get(id):
        return Film.query.filter_by(id=id).one()

    def update(self, id, vals):
        film = self.get(id)

        for key, val in literal_eval(vals).items():
            setattr(film, key, val)

        return film.save()

    @staticmethod
    def create(name, year, pos, rating, url, image):
        film = Film(
            name=name,
            year=year,
            pos=pos,
            rating=rating,
            url=url,
            image=image,
        )

        return film.save()
