#!/usr/bin/python3

""" Define the User class for TimeCapsule
"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv


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
      capsules (relationship): A relationship to the TimeCapsule class, representing the time capsules
        owned by the user.
    """

    _tablename_ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(150), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    capsules = relationship('TimeCapsule', backref='owner', lazy=True)
