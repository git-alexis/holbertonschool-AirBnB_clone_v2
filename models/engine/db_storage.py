from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place

__engine = None
__session = None

def __init__(self):
	""" Initialize the database engine """
	self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
		getenv('HBNB_MYSQL_USER'),
		getenv('HBNB_MYSQL_PWD'),
		getenv('HBNB_MYSQL_HOST'),
		getenv('HBNB_MYSQL_DB'), 
		pool_pre_ping=True
	))
	
	if gentenv('HBNB_ENV') == 'test':
		Base.metadata.drop_all(self.__engine)

