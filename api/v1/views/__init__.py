#!/usr/bin/python3
"""Your first endpoint (route) will be to return the status of your API"""

from flask import Blueprint
app_views = Blueprint('/api/v1', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
