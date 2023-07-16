#!/usr/bin/python3
"""File Storage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """serializes and deserialzes json files"""

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """Return the dictionary of <class>.<id> : object instance"""
        return self.__objects

    def new(self, obj):
        """Add a new object to existing dictionary of instances"""
        if obj:
            keys = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[keys] = obj

    def save(self):
        """Save the object dictionaries to json file"""
        my_dict = {}

        for keys, obj in self.__objects.items():
            """if type(obj) is dict:
            my_dict[keys] = obj
            else:"""
            my_dict[keys] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """If the json file exists, convert object dicts back to instances"""
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)
            for keys, val in new_obj.items():
                obj = self.class_dict[val['__class__']](**val)
                self.__objects[keys] = obj
        except FileNotFoundError:
            pass

