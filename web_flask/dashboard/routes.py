#!/usr/bin/python3

""" A script that creates a flask application"""

# Import the flask library
from flask import render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm


""" Create a route to the registration form"""

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


"""Create a route to the login page"""

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


"""Create a route to the home page"""

@app.route("/home")
def home():
    """A route to the home page of the route"""
    return render_template('home.html', title='Home')


"""Create a route to the error page"""

app.route("/404")
def 404_error():
    return render_template('404_error.html', title='404')
