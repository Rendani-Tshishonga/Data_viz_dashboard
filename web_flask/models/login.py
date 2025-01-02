#!/usr/bin/python3

"""A script that initializes a login table"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class Login(BaseModel, Base):
    __tablename__ = "login"
    username = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
