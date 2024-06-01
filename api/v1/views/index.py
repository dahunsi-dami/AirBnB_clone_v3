#!/usr/bin/python3
""""""

from flask import Flask, Response
from api.v1.views import app_views
from models import storage
import json


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def show():
    response = {"status": "OK"}
    postresponse = json.dumps(response, indent=2) + '\n'
    return Response(postresponse, mimetype='application/json')
