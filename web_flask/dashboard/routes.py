#!/usr/bin/python3

""" A script that creates a flask routes"""

# Import the flask library
from dashboard import app, db, bcrypt
from flask import render_template,url_for, flash, redirect
from dashboard.forms import RegistrationForm, LoginForm
from dashboard.models import User, Products, Order, Shipments, Suppliers
from flask_login import login_user, current_user, logout_user, login_required
import pandas as pd


""" Create a route to the registration form"""

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
@login_required
def home():
    """A route to the home page of the route"""
    return render_template('home.html', title='Home')


"""Create a logout route to handle user sessions"""

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


"""Create a route that will hanle the 404 HTTP error"""

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Page_not_found'), 404


"""Create a products route"""

@app.route("/products")
@login_required
def product():
    product = Products.query.all()
    products = pd.DataFrame(product).to_dict(orient="list")
    return render_template('products.html', title="Products", products=products)

"""Create an order route"""

@app.route("/order")
@login_required
def order():
    order = Order.query.all()
    orders = pd.DataFrame(order).to_dict(orient="list")
    return render_template('order.html', title="Orders", orders=orders)


"""Create a supplier route"""

@app.route("/supplier")
@login_required
def supplier():
    return render_template('suppliers.html', title="Suppliers")


"""Create a shipment route"""

@app.route("/shipment")
@login_required
def shipment():
    return render_template('shipments.html', title="Shipments")
