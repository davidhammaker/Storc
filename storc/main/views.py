from flask import render_template, Blueprint, request
from storc.models import Character


main = Blueprint('main', __name__)


@main.route('/')
def home():
    """
    Render the home page with recent characters.

    :return: 'home.html' template with 10 most recent characters.
    """
    characters = \
        Character.query.filter_by(private=False)\
        .order_by(Character.date.desc()).limit(10)
    return render_template('home.html', characters=characters)


@main.route('/login')
def login():
    """
    Render a list of all login methods.

    :return: 'login.html' template with 'next_page', if any exists.
    """

    # If a 'next' argument exists in the URL, persist the argument.
    next_page = request.args.get('next')

    return render_template('login.html', next_page=next_page)


@main.route('/privacy_policy')
def privacy_policy():
    """
    Render the Privacy Policy.

    :return: 'privacy_policy.txt'.
    """

    return render_template('privacy_policy.html')
