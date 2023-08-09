#!/usr/bin/python3
"""
this is the base model that contains serial/deserial info
"""
from datetime import datetime
import uuid


class BaseModel:
    
    def __init__(self):
        """defining all common attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Helps to update update_at"""
        self.updated_at = datetime.now()
        return self
    
    def to_dict(self):
        """Generate a new dict with an extra field __class__"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """this str prints in human freindry format"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
