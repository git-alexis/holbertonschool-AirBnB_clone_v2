#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
	""" State class """
	__tablename__ = 'states'

	name = Column(String(128), nullable=False)

	if getenv('HBNB_TYPE_STORAGE') == 'db':
		name = Column(String(128), nullable=False)
		cities = relationship("City", backref="state")
	else:
		name = ""

	@property
	def cities(self):
		"""getter attribute cities that returns the list of City instances"""
		cities_list = []
		for city in models.storage.all(City).values():
			if city.state_id == self.id:
				cities_list.append(city)
		return cities_list