#!/usr/bin/python3

""" A script that creates a flask routes"""

# Import the flask library
from dashboard import app, db, bcrypt
from flask import render_template,url_for, flash, redirect
from dashboard.forms import RegistrationForm, LoginForm
from dashboard.models import User
from flask_login import login_user


""" Create a route to the registration form"""

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!, You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


"""Create a route to the login page"""

@app.route("/login", methods=['GET', 'POST'])
def login():
    """A route to the login page of the dashboard"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


"""Create a route to the home page"""

@app.route("/home")
def home():
    """A route to the home page of the route"""
    return render_template('home.html', title='Home')


"""Create a route to the error page"""

@app.route("/404")
def error():
    return render_template('404_error.html', title='404')
