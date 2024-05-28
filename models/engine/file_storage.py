#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import uuid

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""

    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """Update DBStorage and FileStorage"""

        if cls is not None:
            # FileStorage.__objects = cls.to_dict()
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__.__name__ or cls == value.__class__:
                    brt = str(cls)
                    spt = brt.split(".")[-1]
                    last = spt.split("'")[0]
                    anodavalue = FileStorage.__objects[key].to_dict()
                    return (f"[{last}] ({id}) {anodavalue}")
        else:
            return (None)

    def count(self, cls=None):
        """Update DBStorage and FileStorage"""
        i = 0
        j = 0
        classes = {"Amenity": Amenity, "BaseModel": BaseModel,
                   "City": City, "Place": Place,
                   "Review": Review, "State": State, "User": User}
        if cls is not None:
            for key, value in FileStorage.__objects.items():
                if cls == value.__class__.__name__ or cls == value.__class__:
                    anodavalue = FileStorage.__objects[key].to_dict()
                    for srt in anodavalue:
                        i += 1
                    return (i)
        else:
            for key, dclass in classes.items():
                for anod, value in FileStorage.__objects.items():
                    park = value.__class__.__name__
                    pik = value.__class__
                    if dclass == park or dclass == pik:
                        avalue = FileStorage.__objects[anod].to_dict()
                        for srt in avalue:
                            j += 1
                j = j
            return (j)
