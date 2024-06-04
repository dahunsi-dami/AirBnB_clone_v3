#!/usr/bin/python3
"""
Same as State, create a new view for City
"""
from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route("/states/<string:state_id>/cities",
                 methods=['GET'], strict_slashes=False)
def List(state_id):
    """Same as State, create a new view for City"""
    city_list = []
    listc = storage.get(State, state_id)

    if listc is None:
        abort(404)
    for obj in listc.cities:
        city_list.append(obj.to_dict())
    return jsonify(city_list)


@app_views.route("/cities/<string:city_id>",
                 methods=['GET'], strict_slashes=False)
def citylist(city_id):
    """Same as State, create a new view for City"""
    listc = storage.get(City, city_id)
    if listc is None:
        abort(404)
    return jsonify(listc.to_dict())


@app_views.route("/cities/<string:city_id>",
                 methods=["DELETE"], strict_slashes=False)
def deleted(city_id):
    """Same as State, create a new view for City"""
    citye = storage.get(City, city_id)

    if citye is None:
        abort(404)

    storage.delete(citye)
    storage.save()

    return jsonify({}), 200


@app_views.route("states/<string:state_id>/cities",
                 methods=["POST"], strict_slashes=False)
def created(state_id):
    """Same as State, create a new view for City"""
    data = request.get_json(silent=True)
    links = storage.get(State, state_id)

    if links is None:
        abort(404)

    if data is None:
        abort(400, "Not a JSON")

    if 'name' not in data:
        abort(400, "Missing name")

    data["state_id"] = state_id
    new_city = City(**data)
    storage.save()

    return jsonify(new_city.to_dict()), 201


@app_views.route("cities/<string:city_id>",
                 methods=["PUT"], strict_slashes=False)
def puttin(city_id):
    """Same as State, create a new view for City"""
    link = storage.get(City, city_id)

    if link is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")

    ignore = ["id", "state_id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore:
            setattr(link, key, value)
    storage.save()
    return jsonify(link.to_dict()), 200
