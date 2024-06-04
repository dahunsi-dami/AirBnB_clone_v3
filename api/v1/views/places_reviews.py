#!/usr/bin/python3
"""
Same as State, create a new view for City
"""

from flask import abort, Flask, jsonify, request
from api.v1.views import app_views
from models.base_model import BaseModel
from models import storage
from models.review import Review
from models.place import Place


@app_views.route("/places/<string:place_id>/reviews",
                 methods=['GET'], strict_slashes=False)
def List_review(place_id):
    """Same as State, create a new view for City"""
    review_list = []
    listc = storage.get(Place, place_id)

    if listc is None:
        abort(404)
    for obj in listc.reviews:
        review_list.append(obj.to_dict())
    return jsonify(city_list)


@app_views.route("/reviews/<string:review_id>",
                 methods=['GET'], strict_slashes=False)
def reviewlist(review_id):
    """Same as State, create a new view for City"""
    citic = storage.get(Review, review_id)

    if citic is None:
        abort(404)


@app_views.route("/reviews/<string:review_id>",
                 methods=["DELETE"], strict_slashes=False)
def deleted_review(review_id):
    """Same as State, create a new view for City"""
    citye = storage.get(Review, review_id)

    if citye is None:
        abort(404)

    storage.delete(citye)
    storage.save()

    return jsonify({}), 200


@app_views.route("/places/<string:place_id>/reviews",
                 methods=["POST"], strict_slashes=False)
def created_place_review(place_id):
    """Same as State, create a new view for City"""
    data = request.get_json(silent=True)
    links = storage.get(Place, place_id)

    if links is None:
        abort(404)

    if data is None:
        abort(400, "Not a JSON")

    link_user = storage.get(Place, data[user_id])
    if link_user is None:
        abort(404)

    if 'user_id' not in data:
        abort(400, f"Missing {data[user_id]}")

    if 'text' not in data:
        abort(400, "Missing text")

    new_place_review = Review(**data)
    storage.save()

    return jsonify(new_place_review.to_dict()), 201


@app_views.route("/reviews/<string:review_id>",
                 methods=["POST"], strict_slashes=False)
def put_place_review(review_id):
    """Same as State, create a new view for City"""
    link = storage.get(Review, review_id)

    if link is None:
        abort(404)

    data = request.get_json(silent=True)
    if data is None:
        abort(400, "Not a JSON")

    ignore = ["id", "user_id", "place_id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in ignore:
            setattr(link, key, value)
    storage.save()
    return jsonify(link.to_dict()), 200
