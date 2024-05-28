#!/usr/bin/python3
""""""

from models.__init__ import storage
from api.v1.views import app_views
from flask import Flask

app = Flask()
app.register_blueprint(app_views)

@app.teardown_appcontext
def close():
    storage.close()

if __name__ == "__main__":
    if host is not None:
        HBNB_API_HOST = sys.argv[5]
        HBNB_API_PORT = sys.argv[6]
        api.run(host='HBNB_API_HOST', port='HBNB_API_PORT', threaded=True)
    else:
        api.run(host='0.0.0.0', port='5000', threaded=True)
