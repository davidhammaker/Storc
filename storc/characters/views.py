import os
from random import choice
import requests
from flask import (
    render_template, request, flash, Blueprint, redirect, url_for)
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
    character_last = \
        Character.query.order_by(Character.date.desc()).first()
    return render_template(
        'new_character.html',
        name=name,
        gender=gender.title(),
        id=(character_last.id + 1))


@characters.route('/save_character', methods=['GET', 'POST'])
def save_character():
    if request.method == 'POST':
        new_character = request.form
        character = Character(
            name=new_character['name'],
            gender=new_character['gender'],
            height=new_character['height'],
            weight=new_character['weight'],
            hair_color=new_character['hair_color'],
            eye_color=new_character['eye_color'],
            unique_attribute=new_character['unique_attribute'],
            favorite_clothes=new_character['favorite_clothes'],
            hair=new_character['hair'],
            mannerism_one=new_character['mannerism_one'],
            mannerism_two=new_character['mannerism_two'],
            speaking_style=new_character['speaking_style'],
            skill=new_character['skill'],
            flaw=new_character['flaw'],
            fear=new_character['fear'],
            favorite=new_character['favorite'],
            family=new_character['family'],
            friends=new_character['friends'],
            significant_other=new_character['significant_other'],
            user=current_user)
        db.session.add(character)
        db.session.commit()
        flash('Your character has been saved!', 'good')
        return 'Character saved successfully.'
    else:
        character_last = Character.query\
            .order_by(Character.date.desc())\
            .filter_by(user_id=current_user.id)\
            .first()
        return redirect(
            url_for('characters.character', id=character_last.id))


@characters.route('/character/<int:id>')
def character(id):
    character = Character.query.get_or_404(id)
    return render_template(
        'character.html',
        character=character,
        title=character.name)
