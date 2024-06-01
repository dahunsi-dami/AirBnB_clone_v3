#!/usr/bin/python3
"""Your first endpoint (route) will be to return the status of your API"""

from flask import Flask, Response, jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
import json


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def show():
    response = {"status": "OK"}
    postresponse = json.dumps(response, indent=2) + '\n'
    return Response(postresponse, mimetype='application/json')


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def count():
    response = {'amenities': storage.count(Amenity),
                'cities': storage.count(City),
                'places': storage.count(Place),
                'reviews': storage.count(Review),
                'states': storage.count(State),
                'users': storage.count(User)}
    postresponse = json.dumps(response, indent=2) + '\n'
    return Response(postresponse, mimetype='application/json')
