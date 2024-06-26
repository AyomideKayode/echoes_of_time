#!/usr/bin/python3
""" Define the User class for TimeCapsule
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Boolean, DateTime, Text
from sqlalchemy.orm import relationship
import uuid


class TimeCapsule(BaseModel, Base):
    """
    Represents a time capsule object.

    Attributes:
        id (int): The unique identifier of the time capsule.
        title (str): The title of the time capsule.
        description (str): The description of the time capsule.
        created_date (datetime): The date and time when the time capsule
        was created.
        unlock_date (datetime): The date and time when the time capsule
        can be unlocked.
        visibility (bool): Indicates whether the time capsule is
        private or not.
        status (bool): Indicates whethen the time capsule is opened or not.
        user_id (int): The ID of the user who owns the time capsule.
        contents (list): The contents of the time capsule.
    """
    __tablename__ = 'time_capsules'
    user_id = Column(String(200), ForeignKey('users.id'), nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    unlock_date = Column(DateTime, nullable=False)
    # Status of the Capsule (False: unlocked, True: Locked)
    status = Column(Boolean, default=True)
    # Visibility of the Capsule (True: Public, False: Private)
    visibility = Column(Boolean, default=True)
    contents = relationship('Content', backref='time_capsule',
                            lazy=True, cascade='all, delete-orphan')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = uuid.uuid4()
