from dashboard import db
from datetime import datetime

"""
Create Classes which will be mapped to our
database tables.
"""

"""
Create an Orders tables which will be mapped to the 
orders table in our database
"""


class Order(db.Model):
    order_id = db.Column(db.Integer, nullable=False, primary_key=True)
    order_date = db.Column(db.DateTime, nullable, default=datetime.utcnow)
    quantity_ordered = db.Column(db.Integer, nullable=False)

    """Create the __repr__ method that returns a printable representation of the object"""
    def __repr__(self):
        return f'Order("{self.order_id}", "{self.order_date}", "{self.quantity_ordered}")'

"""
Create a product class which will be mapped to the 
products table in our database
"""


class Products(db.Model):
    product_id = db.Column(db.Integer, primary_key=True,  nullable=False)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    unit_price = db.Column(db.Float(5), nullable=False, default=0)
    quantity_available = db.Column(db.Integer, nullable=False)
    
    """Create the __repr__ method that returns a printable representation of the object"""
    def __repr__(self):
        return f'Products("{self.name}", "{self.unit_price}", "{self.quantity_available}")'

"""
Create a Shipment class which will be mapped to the 
shipment table in our database
"""


class Shipments(db.Model):
    shipment_id = db.Column(db.Integer, primary_key=True, nullable=False)
    shipment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    estimated_arrival_date = db.Column(db.DateTime, nulllable=False, default=datetime.utcnow)
    actual_arrival_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    """Create the __repr__ method that returns a printable representation of the object"""
    def __repr__(self):
        return f'Shipments("{self.shipment_date}", "{self.actual_arrival_date}")'

"""
Create a suppliers class which will be mapped to the 
suppliers table in our database
"""

class Suppliers(db.Model):
    supplier_id = db.Column(db.Integer, primary_key=True, nullable=False)
    address = db.Column(db.String(128), nullable=False)
    contact_person = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    
    """Create the __repr__ method that returns a printable representation of the object"""
    def __repr__(self):
        return f'Suppliers("{self.suppplier_id}", "{self.conatct_person}")'
