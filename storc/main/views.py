from flask import render_template, Blueprint
from storc.models import Character


main = Blueprint('main', __name__)


@main.route('/')
def home():
    characters = \
        Character.query.order_by(Character.date.desc()).limit(10)
    return render_template('home.html', characters=characters)
