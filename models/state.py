#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel):
	""" State class """
	if getenv('HBNB_TYPE_STORAGE') == 'db':
		__tablename__ = 'states'
		name = Column(String(128), nullable=False)
		cities = relationship("City", backref="state")
	else:
		name = ""

	@property
	def cities(self):
		"""getter attribute cities that returns the list of City instances"""
		from models import storage
		from models.city import City
		cities = storage.all(City)
		city_list = []
		for city in cities.values():
			if city.state_id == self.id:
				city_list.append(city)
		return city_list