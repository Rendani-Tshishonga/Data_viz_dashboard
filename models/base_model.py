#!/usr/bin/python3

"""
This module defines a base model for the metadata of our models
"""
# import Libraries
from uuid import uuid4
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, dateTime

Base = declarative_base()

class BaseModel:
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
    
    def __str___(self):
        """Returns a string representation of the instance"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Adds and saves the current database object to the database"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
    
    def to_dict(self):
        """Returns a dictionary of all the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict[created_at].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime("Y-%m-%dT%H:%M:%S.%f")
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
    
    def delete(self):
        """Deletes the current instance of storage"""
        models.storage.delete(self)
