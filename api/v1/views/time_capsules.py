#!/usr/bin/python3
"""Time capsules view module"""


from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.time_capsule import TimeCapsule
from api.firebase_config import firebase_auth


@app_views.route('/time_capsules', methods=['GET'], strict_slashes=False)
@firebase_auth
def get_time_capsules():
    """Retrieves the list of all TimeCapsule objects"""
    time_capsules = storage.all(TimeCapsule)
    time_capsules = time_capsules.values()
    time_capsules = [time_capsule.to_dict() for time_capsule in time_capsules]
    return jsonify(time_capsules)


@app_views.route('/time_capsules', methods=['POST'], strict_slashes=False)
@firebase_auth
def post_time_capsule():
    """Creates a TimeCapsule"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    description = data.get('description')
    unlock_date = data.get('unlock_date')
    status = data.get('status')
    visibility = data.get('visibility')

    if not user_id:
        abort(400, 'Missing user_id')
    if not title:
        abort(400, 'Missing title')
    if not description:
        abort(400, 'Missing description')
    if not unlock_date:
        abort(400, 'Missing unlock_date')
    if not status:
        abort(400, 'Missing status')
    if not visibility:
        abort(400, 'Missing visibility')
    time_capsule = TimeCapsule(**data)
    time_capsule.save()
    return jsonify(time_capsule.to_dict()), 201


@app_views.route('/time_capsules/<time_capsule_id>', methods=['GET'],
                 strict_slashes=False)
@firebase_auth
def get_time_capsule(time_capsule_id):
    """Retrieves a TimeCapsule object"""
    time_capsule = storage.get(TimeCapsule, time_capsule_id)
    if time_capsule:
        return jsonify(time_capsule.to_dict())
    abort(404)


@app_views.route('/time_capsules/<time_capsule_id>', methods=['DELETE'],
                 strict_slashes=False)
@firebase_auth
def delete_time_capsule(time_capsule_id):
    """Deletes a TimeCapsule object"""
    time_capsule = storage.get(TimeCapsule, time_capsule_id)
    if time_capsule:
        storage.delete(time_capsule)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/time_capsules/<time_capsule_id>', methods=['PUT'],
                 strict_slashes=False)
@firebase_auth
def put_time_capsule(time_capsule_id):
    """Updates a TimeCapsule object"""
    time_capsule = storage.get(TimeCapsule, time_capsule_id)
    if not time_capsule:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'user_id', 'created_at', 'updated_at']:
            setattr(time_capsule, key, value)
    time_capsule.save()
    return jsonify(time_capsule.to_dict()), 200
