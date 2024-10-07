#!/usr/bin/python3

# Import Libraries
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from models import base_model, order, product, shipment, suppliers

class DBStorage():
    class_dict = {
        "BaseModel": base_model.BaseModel,
        "Orders": order.Orders,
        "Products": product.Products,
        "Shipments": shipment.Shipment,
        "Suppliers": suppliers.Supplier
    }

    # Create Private attributes
    __engine = None
    __session = None

    def __init__(self):
        # Initialize a connection to the mysql database
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('MYSQL_USER'),
                os.environ.get('MYSQL_PWD'),
                os.environ.get('MYSQL_HOST'),
                os.environ.get('MYSQL_DB'),
                pool_pre_ping=True
            )
        )
        if os.environ.get('MYSQL_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def new(self, obj):
        """Add object to current database object"""
        return self.__engine.add(obj)
    
    def save(self):
        """Commit all changes to the current database"""
        return self.__session.commit()
    
    def delete(self, obj=None):
        """Delete from the current database session"""
        if obj is not None:
            return self.__session.delete(obj)
    
    def reload(self):
        """Create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        """Create the current database session"""
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
    
    def get(self, class_dict, id):
        """A method to retrieve an object"""
        object_class = self.all()
        for obj in object_class.values():
            if id == str(obj.id):
                return obj
            else:
                return None
    
    def count(self, class_dict=None):
        """A method to count objects in storage"""
        if class_dict is not None:
            return len(self.all(class_dict))
        else:
            return len(self.all())




