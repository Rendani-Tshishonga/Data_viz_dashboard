#!/usr/bin/python3

"""Testing database connection"""
from sqlalchemy import create_engine
import os

try:
    print("Initializing a database connection")
    create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                os.environ.get('MYSQL_USER'),
                os.environ.get('MYSQL_PWD'),
                os.environ.get('MYSQL_HOST'),
                os.environ.get('MYSQL_DB')
            ))
except Exception as ex:
    print("No database connection")
