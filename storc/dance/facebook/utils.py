import os
import requests
import secrets
from flask import flash
from sqlalchemy.orm.exc import NoResultFound
from flask_dance.contrib.facebook import make_facebook_blueprint
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized, oauth_error
from flask_login import current_user, login_user
from storc import login_manager, db
from storc.models import User, OAuth
from storc.users.utils import upload_profile_picture

# Set up Flask-Dance Facebook blueprint
fb_blueprint = make_facebook_blueprint(
    client_id=os.environ.get("STORC_FB_ID"),
    client_secret=os.environ.get("STORC_FB_SECRET"))


@login_manager.user_loader
def load_user(user_id):
    """Set user_loader callback. Based on Flask-Login and Flask-Dance
    documentation."""
    return User.query.get(int(user_id))


# Set up SQLAlchemy backend
fb_blueprint.backend = SQLAlchemyBackend(
    OAuth, db.session, user=current_user)


@oauth_authorized.connect_via(fb_blueprint)
def facebook_logged_in(blueprint, token):
    """Log in users with Facebook, storing them in the database if they
    are not already stored. Heavily based on Flask-Dance documentation.
    Return False to ensure that Flask-Dance does not save the OAuth
    token by default.

    :param blueprint: a Flask blueprint for Facebook login.
    :param token: the OAuth authentication token.
    :return: False.
    """

    # If no token is given, send a flash message and return False
    if not token:
        flash('Failed to log in with Facebook.', 'bad')
        return False

    # Retrieve user ID and name
    response = blueprint.session.get('/me')

    # If the response is bad, send a flash message and return False
    if not response.ok:
        flash('Failed to fetch user info from Facebook.', 'bad')
        return False

    # If the response is good, store the info as named references
    facebook_info = response.json()
    facebook_user_id = str(facebook_info['id'])

    # Get the profile picture URL
    pic_response = blueprint.session.get(
        f'/{facebook_info["id"]}?fields=picture')
    pic_url = pic_response.json()['picture']['data']['url']

    # Use the profile picture URL to get the picture data
    pic_request = requests.get(pic_url)

    # Search for the user's Facebook ID in the database
    query = OAuth.query.filter_by(
        provider=blueprint.name, provider_user_id=facebook_user_id)
    try:
        oauth = query.one()
    except NoResultFound:
        # If the ID cannot be found, store the ID and token, which will
        # later be committed to the database
        oauth = OAuth(
            provider=blueprint.name,
            provider_user_id=facebook_user_id,
            token=token)

    # If the stored OAuth information (ID and token) is associated with
    # a user, log in that user
    if oauth.user:
        login_user(oauth.user)
        flash('Successfully logged in with Facebook!', 'good')

    # If no user is found, create one
    else:

        # Store the user's profile picture on Dropbox
        pic_filename = f'{secrets.token_hex(8)}.jpeg'
        upload_profile_picture(
        pic_request._content, pic_filename)

        # Generate a random username based on the user's first name
        username = \
            f"{facebook_info['name'].split()[0]}_" \
            f"{secrets.token_hex(3)}".lower()

        # Store the user information
        user = User(
            name=facebook_info['name'].split()[0],
            username=username,
            profile_picture=pic_filename,
            validated=True,
            login='facebook')

        # Associate the user with the OAuth information
        oauth.user = user

        # Commit the User and OAuth info to the database
        db.session.add_all([user, oauth])
        db.session.commit()

        # Log in the user
        login_user(user)

        flash('Successfully signed up with Facebook!', 'good')
    return False


@oauth_error.connect_via(fb_blueprint)
def facebook_error(
        blueprint, error, error_description=None, error_uri=None):
    """
    Display OAuth provider errors. Heavily based on Flask-Dance
    documentation.

    :param blueprint: a Flask blueprint for Facebook login.
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
