#!/usr/bin/python3
"""Your first endpoint (route) will be to return the status of your API"""

from flask import Flask, Response
from api.v1.views import app_views
from models import storage
import json


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def show():
    response = {"status": "OK"}
    postresponse = json.dumps(response, indent=2) + '\n'
    return Response(postresponse, mimetype='application/json')
