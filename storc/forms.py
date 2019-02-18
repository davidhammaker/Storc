from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError)
from storc import db
from storc.models import User


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
        Length(min=6, max=72)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            if user.validated:
                raise ValidationError(
                    'That username is already in use.')
            else:
                db.session.delete(user)
                db.session.commit()

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email address is already in use.')


class EmailVerifyForm(FlaskForm):
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()])
    submit = SubmitField('Submit')


class EmailLoginForm(FlaskForm):
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()])
    password = PasswordField('Password', validators=[
        DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, max=72)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')])
    submit = SubmitField('Submit')
