#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base, BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ DB Engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Class's Constructor """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        url = f"mysql+mysqldb://{user}:{password}@{host}:3306/{database}"
        self.__engine = create_engine(url, pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            Returns a list of all objects of a specific class or
            stored in the database
        """
        dictionary = dict()
        classes = [Amenity, City, Place, Review, State, User]
        if cls in classes:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{type(obj).__name__}.{obj.id}"
                dictionary[key] = obj
            return dictionary
        for classs in classes:
            objects = self.__session.query(classs).all()
            for obj in objects:
                key = f"{type(obj).__name__}.{obj.id}"
                dictionary[key] = obj
        return dictionary

    def new(self, obj):
        """
            Adds a new object to the database
        """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                print(e)

    def save(self):
        """
            Commits all changes to the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
            Deletes from the current database session the object
        """
        if obj is not None:
            self.__session.query(type(obj).__name__).filter(
                type(obj).id == obj.id).delete(synchronize_session=False)

    def reload(self):
        """
            Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)()

    def close(self):
        """
            Closes the connection
        """
        self.__session.close()
