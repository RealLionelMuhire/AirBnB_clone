#! /usr/bin/python3
""" This is the file storage class """
import json


class FileStorage:
    """This class serializes instances to, and
    deserializes instances from , JSON file"""
    __file_path = 'file.json'
    __objects = {}
    
    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
    
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.loads(f.read())
                for value in dict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except Exception:
            pass