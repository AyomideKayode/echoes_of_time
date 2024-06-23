#!/usr/bin/python3
""" Define the User class for TimeCapsule
"""


from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


class User(BaseModel, Base):
    """Define the User class for TimeCapsule.
    This class represents a user in the TimeCapsule system.
    It contains information about the user's
    identity, such as their username, email, and password.
    Additionally, it maintains a relationship
    with the TimeCapsule class, allowing users to own multiple time capsules.

    Attributes:
      id (int): The unique identifier for the user.
      username (str): The username of the user. Must be unique.
      email (str): The email address of the user. Must be unique.
      password (str): The password of the user.
      capsules (relationship): A relationship to the TimeCapsule class,
      representing the time capsules owned by the user.
    """
    __tablename__ = 'users'
    id = Column(String(250), primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)  # Hashed password
    last_login = Column(DateTime, nullable=True)
    capsules = relationship('TimeCapsule', backref='user',
                            lazy=True, cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.password = kwargs['password']

    @property
    def password(self):
        # Prevent password from being accessed
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
