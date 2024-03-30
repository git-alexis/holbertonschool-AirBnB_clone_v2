#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
from models.base_model import BaseModel,Base


class Place(BaseModel, Base):
    """ A place to stay """
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    __tablename__ = 'places'

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []
    
        if getenv('HBNB_TYPE_STORAGE') == 'db':
            reviews = relationship("Review", backref="place", cascade="all, delete", passive_deletes=True)
            amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
        else:
            @property
            def reviews(self):
                """getter attribute cities that returns the list of City instances"""
                reviews_list = []
                for review in models.storage.all(Review).values():
                    if review.place_id == self.id:
                        reviews_list.append(review)
                return reviews_list
            
            @property
            def amenities(self):
                """getter attribute cities that returns the list of City instances"""
                amenities_list = []
                for amenity in models.storage.all(Amenity).values():
                    if amenity.id in self.amenity_ids:
                        amenities_list.append(amenity)
                return amenities_list
            
            @amenities.setter
            def amenities(self, obj):
                """setter attribute cities that returns the list of City instances"""
                if isinstance(obj, Amenity):
                    self.amenity_ids.append(obj.id)