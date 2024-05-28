#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "db":
    from models.engine.test_db import DBStorage
    storage = DBStorage()
else:
    from models.engine.test_file import FileStorage
    storage = FileStorage()
storage.reload()
