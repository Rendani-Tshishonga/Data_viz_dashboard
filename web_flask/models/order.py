#!/usr/bin/python3

# Import libraries
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Order(BaseModel, Base):
    __tablename__ = 'orders'

    order_id = Column(String(60), primary_key=True, nullable=False)
    product_id = Column(String(60), ForeignKey(products.id), nullable=False)
    supplier_id = Column(String(60), ForeignKey(suppliers.id), nullable=False)
    order_date = Column(DateTime, nullable=False, default=datetime.utcnow())
    quantity_ordered = Column(Integer, nullable=False)
    shipments = relationship("Shipment", backref="order", cascade="all, delete, delete-orphan")
