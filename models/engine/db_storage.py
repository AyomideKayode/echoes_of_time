#!/usr/bin/python3

"""Module that defines the DBStorage class for TimeCapsule
Contains the implementation of the DBStorage class, which manages
the storage of timecapsule models in a MySQL database.
It provides methods for querying, adding, deleting,
and saving objects to the database.

Classes:
- DBStorage: Manages storage of timecapsule models in a MySQL database.
"""


from os import getenv
from dotenv import load_dotenv
from sqlalchemy import create_engine
import models
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.time_capsule import TimeCapsule
from models.content import Content

classes = {"User": User, "TimeCapsule": TimeCapsule, "Content": Content}
class DBStorage:
    """This class manages storage of timecapsule models in a MySQL database
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates a new instance of DBStorage
        """
        load_dotenv()
        user = getenv("DB_USER")
        passwd = getenv("PASSWORD")
        host = getenv("HOST")
        db = getenv("DB")
        env_var = getenv('ENV')

        # print(
        #     f"User: {user}, Password: {passwd}, Host: {host}, DB: {db}, Env: {env_var}")
        # print statement for debugging MySQL connection issue

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        try:
            if env_var == 'test':
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    def all(self, cls=None):
        """Query on the current database session (self.__session)
        """

        classes = [BaseModel, User, TimeCapsule, Content]
        objs = {}

        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            for obj in self.__session.query(cls).all():
                objs[obj.__class__.__name__ + '.' + obj.id] = obj
        else:
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    objs[obj.__class__.__name__ + '.' + obj.id] = obj
        return objs

    def new(self, obj):
        """Add the object to the current database session
        """

        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session
        """

        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None
        """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database
        and create the current database session
        """

        Base.metadata.create_all(self.__engine, checkfirst=True)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Method to close the session
        """

        self.__session.close()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
