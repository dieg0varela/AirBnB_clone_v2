#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.expression import column, null
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review
from models import storage
from sys import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                              cascade="all, delete-orphan")
    else:
        @property
        def reviews(self):
            ret = []
            Review_objs = storage.all(Review)
            for key in Review_objs:
                if Review_objs[key].place_id == self.id:
                    ret.append(Review_objs[key])
            return ret
