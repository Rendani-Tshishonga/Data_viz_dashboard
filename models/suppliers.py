#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel, Base

class Supplier(BaseModel, Base):
    __tablename__ = 'suppliers'

    name = Column(String(128), nullable=False)
    address = Column(String(1024), nullable=False)
    contact_person = Column(String(60), nullable=False)
    phone_number = Column(String(128), nullable=False)