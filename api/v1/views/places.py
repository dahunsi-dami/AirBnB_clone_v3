#!/usr/bin/python3
"""
Same as State, create a new view for City
"""
from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.state import State


@app_views.route("/cities/<string:city_id>/places",
                 methods=["GET"], strict_slashes=False, endpoint='listcity')
def listcity(city_id):
    """Same as State, create a new view for City"""
    place_list = []
    lis = storage.get(City, city_id)

    if lis is None:
        abort(404)
    for obj in lis.places:
        place_list.append(obj.to_dict())
    return jsonify(place_list)


@app_views.route("/places/<string:place_id>",
                 methods=["GET"], strict_slashes=False)
def placelist(place_id):
    """Same as State, create a new view for City"""
    citic = storage.get(Place, place_id)

    if citic is None:
        abort(404)
    return jsonify(citic.to_dict())


@app_views.route("/places/<string:place_id>",
                 methods=["DELETE"], strict_slashes=False)
def deleted_place(place_id):
    """Same as State, create a new view for City"""
    citye = storage.get(Place, place_id)

    if citye is None:
        abort(404)

    storage.delete(citye)
    storage.save()

    return jsonify({}), 200


@app_views.route("/cities/<string:city_id>/places",
                 methods=["POST"], strict_slashes=False)
def created_place(city_id):
    """Same as State, create a new view for City"""
    data = request.get_json(silent=True)
    links = storage.get(City, city_id)

    if links is None:
        abort(404)

    if data is None:
        abort(400, "Not a JSON")

    if 'name' not in data:
        abort(400, "Missing name")

    new_data = storage.get(User, data["user_id"])

    if new_data is None:
        abort(404)

    if 'user_id' not in new_data:
        abort(400, "Missing user_id")

    data["city_id"] = city_id
    new_place = Place(**data)
    new_place.save()

    return jsonify(new_place.to_dict()), 201


@app_views.route("/places/<string:place_id>",
                 methods=["PUT"], strict_slashes=False)
def put_place(place_id):
    """Same as State, create a new view for City"""
    link = storage.get(Place, place_id)

    if link is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")

    ignore = ["id", "user_id", "city_id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore:
            setattr(link, key, value)
    storage.save()
    return jsonify(link.to_dict()), 200
