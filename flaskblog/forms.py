from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

# Python classes to create forms
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Complete registration')

    # Function to guarantee only unique usernames
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        # If user already is taken, tell the user
        if user:
            raise ValidationError('Username already taken')

    # Function to guarantee only unique emails
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        # If email already is taken, tell the user
        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log in')


# Class representing form to update account information
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Profile picture', validators=[FileAllowed(['jpg','jpeg','svg','png'])])
    submit = SubmitField('Update')

    # Function to guarantee only unique usernames
    def validate_username(self, username):
        # Make sure user is not changing to his current username
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            # If user already is taken, tell the user
            if user:
                raise ValidationError('Username already taken')

    # Function to guarantee only unique emails
    def validate_email(self, email):
        # Make sure user is not changing to his current username
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            # If email already is taken, tell the user
            if user:
                raise ValidationError('Email already in use')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
