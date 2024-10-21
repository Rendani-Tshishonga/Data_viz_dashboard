#!/usr/bin/python3

""" A script that creates a flask application"""

# Import the flask library
from flask import flask, render_template

# Instantiate the flask application
app = Flask(__name__)

# Create a route to the home_page
@app.route("/")
def login():
    """A route to the login page of the dashboard"""
    return render_template('login.html')

@app.route("/home")
def home():
    """A route to the home page of the route"""
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host=localhost, port=5000, debug=True)