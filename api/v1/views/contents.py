#!/usr/bin/python3
"""Contents view module"""

import os
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.content import Content
from models.time_capsule import TimeCapsule
from api.firebase_config import firebase_auth
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()
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
    type = request.form.get("type")
    description = request.form.get("description")
    if not type or type not in ['image', 'video', 'audio', 'text']:
        abort(400, 'Missing type or Invalid Type')
    if not description:
        abort(400, 'Missing description')
    if 'file' not in request.files:
        abort(400, 'No file part')
    file = request.files['file']
    if file.filename == '':
        abort(400, 'No selected file')
    data = {"type": type, "description": description, "capsule_id": time_capsule_id}
    file_name = file.filename
    absolute_path = os.path.join(time_capsule_id, file_name)
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container='data', blob=absolute_path)
    blob_client.upload_blob(file)
    data['uri'] = blob_client.url
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
