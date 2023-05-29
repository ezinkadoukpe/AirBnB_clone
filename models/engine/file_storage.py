#!/usr/bin/python3

"""This is the file storage class for AirBnB"""

import json
from models.base_model import BaseModel

class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects = {}
    classes = {"BaseModel": BaseModel}

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
        for key, obj in self.__objects.items():
            objdict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    class_obj = eval(class_name)
                    self.__objects[key] = class_obj(**value)
        except FileNotFoundError:
            pass
