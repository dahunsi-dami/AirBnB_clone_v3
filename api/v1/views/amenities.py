#!/usr/bin/python3
""""""

from models.base_model import BaseModel
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from models.amenity import Amenity
from models import storage
import json


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def vie(amenity_id):
    if amenity_id is None:
        amenities = storage.all(Amenity).values()
        lists = [state.to_dict() for amenity in amenities]
        return jsonify(lists)
    else:
        amenity = storage.get(Amenity, amenity_id)
        if amenity is None:
            abort(404)
        return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delet(amenity_id):
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_n():
    data = request.get_json(silent=True)

    if data is None:
        abort(400, "Not a JSON")

    if 'name' not in data:
        abort(400, "Missing name")

    new_amenity = Amenity(**data)
    storage.save()

    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def pute(amenity_id):
    var = storage.get(Amenity, amenity_id)

    if var is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore:
            setattr(var, key, value)
    storage.save()

    return jsonify(var.to_dict()), 200
