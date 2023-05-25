#!/usr/bin/python3

import json
from models.base_model import BaseModel


class FileStorage:
    """ A file Storage class"""

    __file_path = "file.json"
    __objects = {}

    class all(self):
        """returns dictionnary"""
        return self.__objects

    class new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    class save(self):

