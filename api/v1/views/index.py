#!/usr/bin/python3
""" Index """
from models.user import User
from models.time_capsule import TimeCapsule
from models.content import Content
from models import storage
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ Status of API """
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ Stats of API """
    return jsonify({
        "users": storage.count(User),
        "time_capsules": storage.count(TimeCapsule),
        "contents": storage.count(Content)
    })
