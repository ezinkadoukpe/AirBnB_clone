#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """ class BaseModel that defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Instantition"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """string out"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        my_obj = self.__dict__.copy()
        my_obj['__class__'] = self.__class__.__name__
        my_obj['created_at'] = self.created_at.isoformat()
        my_obj['updated_at'] = self.updated_at.isoformat()
        return my_obj
