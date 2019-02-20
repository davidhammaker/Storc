import os
import json
from random import choice
import requests
from flask import render_template, request, flash, Blueprint
from flask_login import current_user
from storc import db
from storc.models import Character


characters = Blueprint('characters', __name__)


@characters.route('/new_character')
def new_character():
    gender = choice(['male', 'female'])
    api_key = os.environ.get('BTN_KEY')
    random_name_url = f'https://www.behindthename.com/api/random.json' \
        f'?usage=eng&number=1&randomsurname=yes&gender={gender[0]}' \
        f'&key={api_key}'
    names_request = requests.get(random_name_url)
    names_list = names_request.json()['names']
    name = f'{names_list[0]} {names_list[1]}'
    return render_template('new_character.html', name=name,
                           gender=gender.title())


@characters.route('/save_character', methods=['POST'])
def save_character():
    new_character = request.form
    character_data =\
        {key: new_character[key] for key in new_character.keys()}
    character =\
        Character(data=json.dumps(character_data), user=current_user)
    db.session.add(character)
    db.session.commit()
    flash('Your character has been saved!', 'good')
    return 'Character saved successfully.'


@characters.route('/character/<id>')
def character(id):
    character = Character.query.get_or_404(id)
    data = json.loads(character.data)
    return render_template(
        'character.html', data=data, character=character)
