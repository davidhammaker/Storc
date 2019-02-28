import os
import requests
import secrets
from flask import flash
from sqlalchemy.orm.exc import NoResultFound
from flask_dance.contrib.google import make_google_blueprint
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_login import current_user, login_user
from storc import login_manager, db
from storc.models import User, OAuth
from storc.users.utils import upload_profile_picture

# Set up Flask-Dance Google blueprint
g_blueprint = make_google_blueprint(
    client_id=os.environ.get("STORC_G_ID"),
    client_secret=os.environ.get("STORC_G_SECRET"))


@login_manager.user_loader
def load_user(user_id):
    """Set user_loader callback. Based on Flask-Login and Flask-Dance
    documentation."""
    return User.query.get(int(user_id))


# Set up SQLAlchemy backend
g_blueprint.backend = SQLAlchemyBackend(
    OAuth, db.session, user=current_user)


@oauth_authorized.connect_via(g_blueprint)
def google_logged_in(blueprint, token):
    """Log in users with Google, storing them in the database if they
    are not already stored. Heavily based on Flask-Dance documentation.
    Return False to ensure that Flask-Dance does not save the OAuth
    token by default.

    :param blueprint: a Flask blueprint for Google login.
    :param token: the OAuth authentication token.
    :return: False.
    """

    # If no token is given, send a flash message and return False
    if not token:
        flash('Failed to log in with Google.', 'bad')
        return False

    # Retrieve user info
    response = blueprint.session.get('/oauth2/v1/userinfo')

    # If the response is bad, send a flash message and return False
    if not response.ok:
        flash('Failed to fetch user info from Google.', 'bad')
        return False

    # If the response is good, store the info as named references
    google_info = response.json()
    google_user_id = str(google_info['id'])

    # Get the profile picture URL
    pic_url = google_info['picture']

    # Use the profile picture URL to get the picture data
    pic_request = requests.get(pic_url)

    # Search for the user's Google ID in the database
    query = OAuth.query.filter_by(
        provider=blueprint.name, provider_user_id=google_user_id)
    try:
        oauth = query.one()
    except NoResultFound:
        # If the ID cannot be found, store the ID and token, which will
        # later be committed to the database
        oauth = OAuth(
            provider=blueprint.name,
            provider_user_id=google_user_id,
            token=token)

    # If the stored OAuth information (ID and token) is associated with
    # a user, log in that user
    if oauth.user:
        login_user(oauth.user)
        flash('Successfully logged in with Google!', 'good')

    # If no user is found, create one
    else:

        # Store the user's profile picture on Dropbox
        pic_filename = f'{secrets.token_hex(8)}.jpeg'
        upload_profile_picture(pic_request._content, pic_filename)

        # Generate a random username based on the user's first name
        username = \
            f"{google_info['name'].split()[0]}_" \
            f"{secrets.token_hex(3)}".lower()

        # Store the user information
        user = User(
            name=google_info['name'].split()[0],
            username=username,
            profile_picture=pic_filename,
            validated=True,
            login='google')

        # Associate the user with the OAuth information
        oauth.user = user

        # Commit the User and OAuth info to the database
        db.session.add_all([user, oauth])
        db.session.commit()

        # Log in the user
        login_user(user)

        flash('Successfully signed up with Google!', 'good')
    return False


@oauth_error.connect_via(g_blueprint)
def google_error(
        blueprint, error, error_description=None, error_uri=None):
    """
    Display OAuth provider errors. Heavily based on Flask-Dance
    documentation.

    :param blueprint: a Flask blueprint for Google login.
    :param error: a provided error.
    :param error_description: the error's description.
    :param error_uri: the error's URI.
    """
    message = \
        'Oauth error from {name}! Error = {error} description = ' \
        '{description} uri={uri}'.format(
            name=blueprint.name,
            error=error,
            description=error_description,
            uri=error_uri)
    flash(message, 'bad')
