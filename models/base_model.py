#!/usr/bin/python3

"""
This module defines a base model for the metadata of our models
"""
# import Libraries
from uuid import uuid4
from datetime import datetime
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
        return self.__dict__
    
    def save(self):
        """updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.utcnow()
    
    def delete(self):
        """Deletes the current instance of storage"""
        self.delete()
