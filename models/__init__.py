#!/usr/bin/python3

"""This module initializes the models package
"""

from os import getenv
from models import db_storage


db_storage_type = db_storage.DBStorage()

if db_storage_type == 'db':
    storage = db_storage.DBStorage()
    storage.reload()
