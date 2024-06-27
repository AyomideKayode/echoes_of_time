#!/usr/bin/python3
""" This module is used to load the environment variables from the .env file"""


from functools import wraps
from dotenv import load_dotenv
import os
from flask import request, abort


load_dotenv()
API_KEY = os.getenv("API_KEY")

def require_api_key(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")
        if not api_key:
            abort(401)
        if api_key != API_KEY:
            abort(403)
        return view(*args, **kwargs)
    return wrapped_view
