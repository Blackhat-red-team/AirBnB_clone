#!/usr/bin/python3

import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    __file_path = "./file.json"
    __objects = {}
    __models = {
        'User': User,
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):

        return self.__objects

    def new(self, obj):

        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):

        to_json = ""
        dozt1 = {}
        for key, value in self.__objects.items():
            dozt1[key] = value.to_dict()
        to_json = json.dumps(dozt1)
        with open(self.__file_path, "w") as f:
            f.write(to_json)
    def reload(self):

        dozt1 = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                dozt1 = json.loads(f.read())

            for key, obj_dict in dozt1.items():
                cls = globals()[obj_dict['__class__']]
                self.__objects[key] = cls(**obj_dict)
    
