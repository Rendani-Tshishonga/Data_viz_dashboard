#!/usr/bin/python3

""" A script that creates a flask application"""

# Import the flask library
from flask import flask, render_template

# Instantiate the flask application
app = Flask(__name__)

# Create a route to the home_page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host=localhost, port=5000, debug=True)