#!/usr/bin/python3
""""""

from models.base_model import BaseModel
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models.user import User
from models import storage
import json


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def vuser(user_id):
    if user_id is None:
        users = storage.all(User).values()
        lists = [user.to_dict() for user in users]
        return jsonify(lists)
    else:
        user = storage.get(User, user_id)
        if user is None:
            abort(404)
        return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def duser(user_id):
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    storage.delete(user)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    data = request.get_json(silent=True)

    if data is None:
        abort(400, "Not a JSON")

    if 'name' not in data:
        abort(400, "Missing name")

    new_user = User(**data)
    storage.save()

    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<string:user_id>', methods=['PUT'],
                 strict_slashes=False)
def put_user(user_id):
    var = storage.get(User, user_id)

    if var is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(var, key, value)
    storage.save()

    return jsonify(var.to_dict()), 200
