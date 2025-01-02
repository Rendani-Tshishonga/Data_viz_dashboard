
from flask import Flask
from models.engine.db_storage import DBStorage

"""Initialize the application instances"""

storage = DBStorage()
app = Flask(__name__)
