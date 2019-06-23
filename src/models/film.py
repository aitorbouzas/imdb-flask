from . import db
from .abc import BaseModel, MetaBaseModel


class Film(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = "film"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    year = db.Column(db.Integer)
    pos = db.Column(db.Integer)
    rating = db.Column(db.Float)
    url = db.Column(db.String(500))
    image = db.Column(db.String(500))

    def __init__(self, name, year, pos, rating, url, image):
        self.name = name
        self.year = year
        self.pos = pos
        self.rating = rating
        self.url = url
        self.image = image
