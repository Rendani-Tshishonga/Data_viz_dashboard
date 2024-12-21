#!/usr/bin/python3

""" A script that creates a flask application"""

# Import the flask library
from flask import Flask, render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import secrets


# Instantiate the flask application
app = Flask(__name__)


# Create a secret key that is 16 bytes in size
app.config['SECRET_KEY'] = secrets.token_hex(16)


# Create a route to the registration form
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


# Create a route to the login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    """A route to the login page of the dashboard"""
    form = LoginForm()
    if form.validate_on_submit():
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Please enter correct credentials', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/home")
def home():
    """A route to the home page of the route"""
    return render_template('home.html', title='Home')


if __name__ == "__main__":
    app.run(debug=True)
