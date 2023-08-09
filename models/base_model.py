#!/usr/bin/python3
import datetime
import uuid


class BaseModel:
    
    def __init__(self):
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.datetime.now()
        return self
    
    def to_dict(self):
        return self.__dict__
    