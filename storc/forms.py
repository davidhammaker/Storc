from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField)
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, ValidationError)
from flask_login import current_user
from storc import db
from storc.models import User


class EmailRegistrationForm(FlaskForm):
    """A form for user registration via email."""
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
        """
        Check a user's username entry for duplicates.

        :param username: The user's requested username.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            if user.validated:
                raise ValidationError(
                    'That username is already in use.')
            else:
                db.session.delete(user)
                db.session.commit()

    def validate_email(self, email):
        """
        Check a user's email address entry for duplicates.

        :param email: The user's requested email address.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email address is already in use.')


class EmailVerifyForm(FlaskForm):
    """A form for requesting a URL for email address verification."""
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()])
    submit = SubmitField('Submit')


class EmailLoginForm(FlaskForm):
    """A form for user login via email."""
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()])
    password = PasswordField('Password', validators=[
        DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')


class ResetPasswordForm(FlaskForm):
    """A form for requesting a password reset email."""
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=6, max=72)])
    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password')])
    submit = SubmitField('Submit')


class EmailSettingsForm(FlaskForm):
    """A form for updating user account information."""
    name = StringField('First Name', validators=[
        DataRequired(),
        Length(max=32)])
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=32)])
    email = StringField('Email Address', validators=[
        DataRequired(),
        Email()])
    profile_picture = FileField('Profile Picture', validators=[
        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save Changes')

    def validate_username(self, username):
        """
        Check a user's username entry for duplicates.

        :param username: The user's requested username.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            if user != current_user:
                if user.validated:
                    raise ValidationError(
                        'That username is already in use.')
                else:
                    db.session.delete(user)
                    db.session.commit()

    def validate_email(self, email):
        """
        Check a user's email address entry for duplicates.

        :param email: The user's requested email address.
        """
        user = User.query.filter_by(email=email.data).first()
        if user:
            if user != current_user:
                raise ValidationError(
                    'That email address is already in use.')


class AlternateSettingsForm(FlaskForm):
    """A form for updating non-email user account information."""
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=2, max=32)])
    profile_picture = FileField('Profile Picture', validators=[
        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Save Changes')

    def validate_username(self, username):
        """
        Check a user's username entry for duplicates.

        :param username: The user's requested username.
        """
        user = User.query.filter_by(username=username.data).first()
        if user:
            if user != current_user:
                if user.validated:
                    raise ValidationError(
                        'That username is already in use.')
                else:
                    db.session.delete(user)
                    db.session.commit()
