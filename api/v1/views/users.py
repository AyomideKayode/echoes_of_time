#!/usr/bin/python3
"""Users view module"""


from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User
from datetime import datetime
from api.firebase_config import firebase_auth


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users = storage.all(User)
    return jsonify([user.to_dict() for user in users.values()])


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates a User"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    id = data.get('id')
    username = data.get('username')
    email = data.get('email')
    last_login = data.get('last_login')

    if not id:
        abort(400, 'Missing id')
    if not username:
        abort(400, 'Missing username')
    if not email:
        abort(400, 'Missing email')
    if not last_login:
        abort(400, 'Missing last_login')
    date_strFormat = '%Y-%m-%dT%H:%M:%SZ'
    data['last_login'] = datetime.strptime(data['last_login'], date_strFormat)
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object"""
    user = storage.get(User, user_id)
    if user:
        return jsonify(user.to_dict())
    abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if user:
        storage.delete(user)
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """Updates a User object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at', 'email']:
            setattr(user, key, value)
            # last_login should be updated as a datetime object
    user.save()
    return jsonify(user.to_dict()), 200


@app_views.route('/users/<user_id>/time_capsules', methods=['GET'],
                 strict_slashes=False)
@firebase_auth
def get_user_time_capsules(user_id):
    """Retrieves the list of all TimeCapsule objects of a User"""
    user = storage.get(User, user_id)
    if user:
        capsules = [time_capsule.to_dict() for time_capsule in user.capsules]
        return jsonify(capsules)
    abort(404)
