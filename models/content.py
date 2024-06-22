#!/usr/bin/python3
""" Define the User class for TimeCapsule
"""


from base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text


class Content(BaseModel, Base):
    __tablename__ = 'contents'
    capsule_id = Column(String(200), ForeignKey(
                        'time_capsule.id'), nullable=False)
    type = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    # URI for stored media
    uri = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
