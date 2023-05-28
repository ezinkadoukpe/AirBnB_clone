#!/usr/bin/python3

"""This is the file storage class for AirBnB"""

import json
from models.base_model import BaseModel

class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return dictionnary"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objdict = {}
        for key, value in __objects.items():
            objdict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf8') as f:
            json.dump(objdict, f)

    def relaod(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, objt in data.items():
                    class_name, obj_id = key.split(".")
                    obj = globals()[class_name].from_dict(obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass