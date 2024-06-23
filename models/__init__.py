#!/usr/bin/python3
"""This module initializes the models package
"""


from models.engine import db_storage


storage = db_storage.DBStorage()
storage.reload()
