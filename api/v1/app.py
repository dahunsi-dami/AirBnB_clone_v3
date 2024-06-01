#!/usr/bin/python3
"""Your first endpoint route will be to return the status of your API"""

from models import storage
from api.v1.views import app_views
from flask import Flask
import os

storage_t = os.environ.get('HBNB_TYPE_STORAGE')
host = os.getenv('HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(ore):
    storage.close()


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
