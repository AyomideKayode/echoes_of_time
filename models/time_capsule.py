#!/usr/bin/python3

""" Define the User class for TimeCapsule
"""
from models.base_model import Base, BaseModel
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, Text, func
from sqlalchemy.orm import relationship
from os import getenv


class TimeCapsule(BaseModel, Base):
  """
  Represents a time capsule object.

  Attributes:
    id (int): The unique identifier of the time capsule.
    title (str): The title of the time capsule.
    description (str): The description of the time capsule.
    created_date (datetime): The date and time when the time capsule was created.
    unlock_date (datetime): The date and time when the time capsule can be unlocked.
    is_private (bool): Indicates whether the time capsule is private or not.
    user_id (int): The ID of the user who owns the time capsule.
    contents (list): The contents of the time capsule.
  """

  id = Column(Integer, primary_key=True)
  title = Column(String(150), nullable=False)
  description = Column(Text, nullable=True)
  created_date = Column(DateTime, nullable=False,
              default=func.current_timestamp())
  unlock_date = Column(DateTime, nullable=False)
  is_private = Column(Boolean, default=True)
  user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
  contents = relationship('Content', backref='capsule', lazy=True)
