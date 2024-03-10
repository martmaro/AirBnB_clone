#!/usr/bin/python3

"""Define the BaseModel class"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """BaseModel of the AirBnB clone project"""

    def __init__(self, *args, **kwargs):
        """Initialize the Base Model
        
        Arguments: 
            *args: Not used.
            **kwargs (dictionary): Key/value pairs of attributes.
        
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, timeformat))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)


    def save(self):
        """Updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance"""
        retdict = self.__dict__.copy()
        retdict["created_at"] = self.created_at.isoformat()
        retdict["updated_at"] = self.updated_at.isoformat()
        retdict["__class__"] = self.__class__.__name__
        return retdict
    
    def __str__(self):
        """Returns/print: [<class name>] (<self.id>) <self.__dict__>"""
        class_name = self.__class__.__name__
        return "[] ({}) {}".format(class_name, self.id, self.__dict__)
