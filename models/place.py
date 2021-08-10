#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Table
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Float, Integer, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
from models import storage
from os import getenv


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
    place_amenity = Table('place_amenity', Base.metadata,
                          Column(
                                 'place_id', String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True,
                                 nullable=False
                                 ),
                          Column(
                                 'amenity_id', String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False
                                 ),)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            ret = []
            Review_objs = storage.all(Review)
            for key in Review_objs:
                if Review_objs[key].place_id == self.id:
                    ret.append(Review_objs[key])
            return ret

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            if type(value) != Amenity:
                return
            self.amenity_ids = []
            amenity_objs = storage.all(Amenity)
            for key in amenity_objs:
                if amenity_objs[key].amenity_id == self.id:
                    self.amenity_ids.append(amenity_objs[key].id)
