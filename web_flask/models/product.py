#!/usr/bin/python3

"""
A product class which will be mapped to a mysql database.
"""
# Import Libraries
from sqlalchemy import Column, String, Float
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Product(BaseModel, Base):
    __tablename__ = 'products'

    product_id = Column(String(60), primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(1024), nullable=True)
    unit_price = Column(Float(5), nullable=False, default=0)
    quantity_available = Column(Integer, nullable=False)
    orders = relationship("Order", backref="product", cascade="all, delete, delete-orphan")