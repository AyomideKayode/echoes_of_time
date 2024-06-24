#!/usr/bin/python3
""" Firebase configuration file """


import firebase_admin
from firebase_admin import credentials
from flask import request, jsonify
from functools import wraps
from firebase_admin import auth

def firebase_config():
    cred = credentials.Certificate("../echoes-of-time-firebase-adminsdk-n7b6f-c93d2837c5.json")
    firebase_admin.initialize_app(cred)

def firebase_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({"error": "Unauthorized"}), 401
        try:
            auth_token = request.headers['Authorization']
            user = auth.verify_id_token(auth_token)
            return f(*args, **kwargs)
        except Exception as e:
            return {"error": str(e)}, 403
    return wrapper
