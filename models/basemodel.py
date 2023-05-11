#!/usr/bin/python3

"""Defines a base model class"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """the base model of the console"""

    def __init__(self):
        """initialiser"""
        self.id = str(uuid.uuif4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """update updated_at with the current time"""
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string represnetation of the instance"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """
        Returns a dictionary with keys and values of the instance
        created_at and updated_at are converted to string object in ISO format 
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
