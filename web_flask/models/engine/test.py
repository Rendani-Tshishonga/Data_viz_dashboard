#!/usr/bin/python3

"""Testing a coonection to a mysql server"""
from sqlalchemy import create_engine
import os

def get_connection():
    return create_engine(
            "msql+mysqldb://{}:{}@{}:{}/{}".format(
                os.environ.get('MYSQL_USER'),
                os.environ.get('MYSQL_PWD'),
                os.environ.get('MYSQL_HOST'),
                os.environ.get('MYSQL_PORT'),
                os.environ.get('MYSQL_DB')
            )
        )
if __name__ == '__main__':
    try:
        engine = get_connection()
        print("Connection to the {} for user {} created successfully.".format(
            os.environ.get(MYSQL_HOST),
            os.environ.get(MYSQL_USER)
        ))

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
