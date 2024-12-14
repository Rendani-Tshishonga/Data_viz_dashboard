from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

""" A class that registers a user"""
class RegistrationForm(FlaskForm):
    username = StringField('Username',                                                                                                                          validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',                                                                                                                  validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up') 

""" A class that logins to a form"""
class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')
