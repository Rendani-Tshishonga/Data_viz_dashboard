#!/usr/bin/python3

# Import Libraries
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey
from models.base_model import BaseModel, Base

class Shipment(BaseModel, Base):
    __tablename__ = 'shipments'

    shipment_id = Column(String(60), nullable=False)
    order_id = Column(String(60), ForeignKey(orders.id), nullable=False)
    shipment_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    estimated_arrival_date = Column(DateTime, nullable=False)
    actual_arrival_date = Column(DateTime, nullable=False)
