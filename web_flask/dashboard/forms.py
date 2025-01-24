from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from dashboard.models import User

""" A class that registers a user"""

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Please choose a different username, this username is taken!')


""" A class that logins a user into the application"""
class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember  = BooleanField('Remember Me')
    submit = SubmitField('Login')


""" A class that creates a new supplier and posts it to the application"""
class SupplierForm(FlaskForm):
    company_name = StringField('Company Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    contact_person = StringField('Contact Name', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=12)])
    submit = SubmitField('Submit')


""" A class that helps a user update account information"""
class UpdateAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different username')

""" A class that saves a file to a specific path"""
class FileForm(FlaskForm):
    file = FileField('Upload file', validators=[FileAllowed(['csv', 'json'])])
    submit = SubmitField('Upload')

