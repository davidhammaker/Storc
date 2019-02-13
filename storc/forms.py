from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import DataRequired, Length, Email, EqualTo


class EmailRegistrationForm(FlaskForm):
    name = StringField('First Name', validators=[
        Length(max=32)])
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=32)])
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(max=72)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')])
    submit = SubmitField('Submit')


class EmailLoginForm(FlaskForm):
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()])
    password = PasswordField('Password', validators=[
        DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')
