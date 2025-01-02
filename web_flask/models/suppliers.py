#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Supplier(BaseModel, Base):
    __tablename__ = 'suppliers'

    name = Column(String(128), nullable=False)
    address = Column(String(1024), nullable=False)
    contact_person = Column(String(60), nullable=False)
    phone_number = Column(String(128), nullable=False)
    orders = relationship("Order", backref="supplier", cascade="all, delete, delete-orphan")