#!/usr/bin/python3
""""""

from models.base_model import BaseModel
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models.state import State
from models import storage
import json


@app_views.route('/states/', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<string:id>', methods=['GET'], strict_slashes=False)
def view(id=None):
    if id is None:
        states = storage.all(State).values()
        lists = [state.to_dict() for state in states]
        return jsonify(lists)
    else:
        state = storage.get(State, id)
        if state is None:
            abort(404)
        return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete(state_id):
    state = storage.get(State, str(state_id))
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def create_name():
    data = request.get_json()

    if data is None:
        abort(400, decription="Not a json")

    if 'name' not in data:
        abort(400, description="Missing name")

    new_state = State(**data)
    storage.new(new_state)
    storage.save()

    return jsonify(new_state.to_dict()), 200


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def putin(state_id):
    var = storage.get(State, str(state_id))

    if var is None:
        abort(404, description="Not a json")

    data = request.get_json()
    if data is None:
        abort(400, description="Not a json")

    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(var, key, value)
    storage.save()

    return jsonify(var.to_dict()), 200
