#!/usr/bin/python3
""" Blueprint for api v1 """
from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.time_capsules import *
from api.v1.views.contents import *


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
