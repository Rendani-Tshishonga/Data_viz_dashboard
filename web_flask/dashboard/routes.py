#!/usr/bin/python3

""" A script that creates a flask routes"""

# Import the flask library
from dashboard import app, db, bcrypt
from flask import render_template,url_for, flash, redirect, request
from dashboard.forms import (RegistrationForm, LoginForm, SupplierForm,
                             UpdateAccount, FileForm, ResetUserCredentialsForm, ResetPasswordForm)
from dashboard.models import User, Products, Order, Shipments, Suppliers
from flask_login import login_user, current_user, logout_user, login_required
import os
import secrets
from werkzeug.utils import secure_filename


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
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else  redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


"""Create a route to the home page"""
@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
@login_required
def home():
    """A route to the home page of the route"""
    form = FileForm()
    if form.validate_on_submit():
        uploaded_file = form.file.data
        filename = secure_filename(uploaded_file.filename)
        if filename != '':
            form.file.data.save(filename)
        flash('Your file has been uploaded', 'success')
        return redirect(url_for('home'))
    return render_template('home.html', title='Home', form=form)


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
    product = Products.query
    return render_template('products.html', title="Products", product=product)

"""Create an order route"""

@app.route("/order")
@login_required
def order():
    order = Order.query
    return render_template('order.html', title="Orders", order=order)


"""Create a supplier route"""

@app.route("/supplier")
@login_required
def supplier():
    supplier = Suppliers.query
    return render_template('suppliers.html', title="Suppliers", supplier=supplier)

"""Create a new supplier route"""
@app.route("/supplier/new", methods=['GET', 'POST'])
@login_required
def new_supplier():
    form = SupplierForm()
    if form.validate_on_submit():
        supplier = Suppliers(company_name=form.company_name.data, address=form.address.data,
                             contact_person=form.contact_person.data, phone_number=form.phone_number.data)
        db.session.add(supplier)
        db.session.commit()
        flash('A new supplier has been created successfully!', 'success')
        return redirect(url_for('supplier'))
    return render_template('create_supplier.html', title="New Supplier", form=form)


"""Create a shipment route"""

@app.route("/shipment")
@login_required
def shipment():
    return render_template('shipments.html', title="Shipments")


"""Create a route for the user account"""

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccount()
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('accounts.html', title='Account', form=form)
