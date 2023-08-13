#! /usr/bin/python3
""" This is the file storage class """
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """This class serializes instances to, and
    deserializes instances from , JSON file"""
    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w+') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()
                       }, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except Exception:
            pass
