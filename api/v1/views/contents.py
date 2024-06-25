#!/usr/bin/python3
"""Contents view module"""


from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.content import Content
from models.time_capsule import TimeCapsule
from api.firebase_config import firebase_auth


@app_views.route('/time_capsules/<time_capsule_id>/contents', methods=['GET'],
                 strict_slashes=False)
@firebase_auth
def get_contents(time_capsule_id):
    """Retrieves the list of all Content objects"""
    time_capsule = storage.get(TimeCapsule, time_capsule_id)
    if time_capsule:
        contents = [content.to_dict() for content in time_capsule.contents]
        return jsonify(contents)
    abort(404)


@app_views.route('/time_capsules/<time_capsule_id>/contents', methods=['POST'],
                 strict_slashes=False)
@firebase_auth
def post_content(time_capsule_id):
    """Creates a Content"""
    time_capsule = storage.get(TimeCapsule, time_capsule_id)
    if not time_capsule:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    capsule_id = data.get('capsule_id')
    type = data.get('type')
    description = data.get('description')
    # uri should be created here
    content = Content(**data)
    content.save()
    return jsonify(content.to_dict()), 201


@app_views.route('/time_capsules/<time_capsule_id>/contents/<content_id>',
                 methods=['GET'], strict_slashes=False)
@firebase_auth
def get_content(time_capsule_id, content_id):
    """Retrieves a Content object"""
    time_capsule = storage.get(TimeCapsule, time_capsule_id)
    if not time_capsule:
        abort(404)
    content = storage.get(Content, content_id)
    if content:
        return jsonify(content.to_dict())
    abort(404)
