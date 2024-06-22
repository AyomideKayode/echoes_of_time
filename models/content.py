#!/usr/bin/python3

""" Define the User class for TimeCapsule
"""
from models.base_model import Base, BaseModel
from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from os import getenv


class Content(BaseModel, Base):
    id = Column(Integer, primary_key=True)
    content_type = Column(String(50), nullable=False)
    content_value = Column(Text, nullable=False)
    capsule_id = Column(Integer, ForeignKey(
        'time_capsule.id'), nullable=False)
    # URL for stored media
    content_url = Column(String(255), nullable=True)
