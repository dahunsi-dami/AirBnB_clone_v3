#!/usr/bin/python3
"""Same as State, create a new view for City objects that handles"""

from models.base_model import BaseModel
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models.state import State
from models import storage


@app_views.route("/states/<string:state_id>/cities",
                 methods=['GET'], strict_slashes=False)
def List(state_id):
    listc = storage.get(State, state_id)

    if listc is None:
        abort(404)


@app_views.route("/cities/<city_id>",
                 methods=['GET'], strict_slashes=False)
def citylist(city_id):
    citic = storage.get(City, state_id)

    if citic is None:
        abort(404)


@app_views.route("/cities/<city_id>",
                 methods=["DELETE"], strict_slashes=False)
def deleted(city_id):
    citye = storage.get(City, city_id)

    if citye is None:
        abort(404)

    storage.delete(city)
    storage.save()

    return jsonify({}), 200


@app_views.route("states/<state_id>/cities",
                 methods=["POST"], strict_slashes=False)
def created(state_id):
    data = request.get_json(silent=True)
    links = storage.get(State, state_id)

    if links is None:
        abort(404)

    if data is None:
        abort(400, "Not a JSON")

    if 'name' not in data:
        abort(400, "Missing name")

    new_city = City(**data)
    storage.save()

    return jsonify(new_city.to_dict()), 201


@app_views.route("cities/<city_id>",
                 methods=["POST"], strict_slashes=False)
def puttin(city_id):
    link = storage.get(City, city_id)

    if link is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")

    ignore = ["id", "state_id", "updated_at"]
    for key, value in data.items():
        if key not in ignore:
            setattr(link, key, value)
    storage.save()
    return jsonify(link.to_dict()), 200
