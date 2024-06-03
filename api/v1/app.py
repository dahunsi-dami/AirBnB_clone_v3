#!/usr/bin/python3
"""Your first endpoint route will be to return the status of your API"""

from models import storage
from api.v1.views import app_views
from flask import Flask
from flask_cors import CORS
import os
from flask import jsonify, Response
import json

storage_t = os.environ.get('HBNB_TYPE_STORAGE')
host = os.getenv('HOST', '0.0.0.0')
port = int(os.getenv('HBNB_API_PORT', 5000))

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(ore):
    storage.close()


@app.errorhandler(404)
def hint(exception):
    rent = {
        "error": "Not found"
    }
    res = jsonify(rent)
    res.status_code = 404

    return res


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
