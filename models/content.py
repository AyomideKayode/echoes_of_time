#!/usr/bin/python3
""" Define the User class for TimeCapsule
"""


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text


class Content(BaseModel, Base):
  """ Represents a content object in a time capsule.
  This class represents a content object that can be stored in a time capsule.
  It contains information such as the capsule ID, type, description, and URI for stored media.
  Attributes:
    capsule_id (str): The ID of the time capsule that this content belongs to.
    type (str): The type of the content.
    description (str): The description of the content.
    uri (str): The URI for the stored media.
  """
  __tablename__ = 'contents'
  capsule_id = Column(String(200), ForeignKey(
            'time_capsule.id'), nullable=False)
  type = Column(String(50), nullable=False)
  description = Column(Text, nullable=True)
  # URI for stored media
  uri = Column(String(255), nullable=False)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
