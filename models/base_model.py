#!/usr/bin/python3
"""
this is the base model that contains serial/deserial info
"""
from datetime import datetime
import uuid
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        """defining all common attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
                        self.__dict__[key] = datetime.strptime(value, FORMAT)
                    elif key[0] == "id":
                        self.__dict__[key] = str(value)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def save(self):
        """Helps to update update_at"""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Generate a new dict with an extra field __class__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """this str print class Tnts in human freindry format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
