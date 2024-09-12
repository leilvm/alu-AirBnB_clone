#!usr/bin/python3
""" 
Define 'BaseModel' Class 
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A base model class to inherit common functionalities.
    """
    
    def __init__(self):
        self.name = "BaseModel"
    
    def print_name(self):
        print(self.name)

    def save(self):
                self.updated_at = datetime.today()
                models.storage.save()
    
    def to_dict(self):
"""Return dictionary representation of model instance"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.class__.__name__
        return rdict

    def __str__(self):
        """return string representation of the model instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
