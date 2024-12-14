#!/usr/bin/python3

""" A script that creates a flask application"""

# Import the flask library
from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm
import secrets


# Instantiate the flask application
app = Flask(__name__)


# Create a secret key that is 16 bytes in size
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Create a route to the registration form
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


# Create a route to the login page
@app.route("/login")
def login():
    """A route to the login page of the dashboard"""
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/home")
def loginUser():
    """A route to the home page of the route"""
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
