import os
from random import choice
import requests
from flask import (
    render_template, request, flash, Blueprint, redirect, url_for,
    abort)
from flask_login import current_user, login_required
from storc import db
from storc.models import User, Character, Favorite
from storc.users.utils import get_profile_picture


characters = Blueprint('characters', __name__)


@characters.route('/new_character')
def new_character():
    """
    Render a template for generating random characters.

    :return: 'new_character.html' template with a name, gender, and id.
    """

    # Use supplied gender, if possible
    gender = request.args.get('gender')

    # Select a random gender if none is provided
    if not gender:
        gender = choice(['male', 'female'])

    # Use the gender to fetch a random name from Behind the Name
    api_key = os.environ.get('BTN_KEY')
    random_name_url = f'https://www.behindthename.com/api/random.json' \
        f'?usage=eng&number=1&randomsurname=yes&gender={gender[0]}' \
        f'&key={api_key}'
    names_request = requests.get(random_name_url)
    names_list = names_request.json()['names']
    name = f'{names_list[0]} {names_list[1]}'
    return render_template(
        'new_character.html',
        name=name,
        gender=gender.title(),
        character=None)


@characters.route('/save_character', methods=['GET', 'POST'])
@login_required
def save_character():
    """
    Store Character instances in the database, or redirect to a user's
    most recently saved Character.

    :return: message of success or redirect to 'characters.character'
    with a Character id.
    """

    # On a post request, save the posted data as a new character
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

        # The post came from 'static/main.js', and the returned string
        # is a response telling JavaScript that the post was successful
        return 'Character saved successfully.'

    # On a GET request, determine the user's most recent character and
    # redirect the user to that character's page
    else:
        character_last = Character.query\
            .order_by(Character.date.desc())\
            .filter_by(user_id=current_user.id)\
            .first()
        return redirect(
            url_for('characters.character', id=character_last.id))


@characters.route('/character/<int:id>')
def character(id):
    """
    Render a template that displays a generated Character from the
    database.

    :param id: the Character id.
    :return: 'character.html' template with a Character and a title, or
    an abort with a 403.
    """
    character = Character.query.get_or_404(id)

    # Prevent other users from viewing if private
    if character.private and current_user != character.user:
        return abort(403)

    image_path = get_profile_picture(character.user)

    return render_template(
        'character.html',
        character=character,
        title=character.name,
        image_path=image_path)


@characters.route('/all_characters')
def all_characters():
    """
    Render a template that displays a paginated view of all non-private
    characters in alphabetical order, listing 20 characters at a time.

    :return: 'all_characters.html' template with a list of up to 20
    characters.
    """
    page = request.args.get('page_num', 1, type=int)
    gender = request.args.get('gender')
    username = request.args.get('user')
    user = User.query.filter_by(username=username).first()

    # If 'user' query parameter exists, only show characters by that
    # user
    if user:

        # If 'user' is current user, include private characters
        if current_user == user:
            characters = Character.query.order_by(Character.name)\
                .filter_by(user=user)\
                .paginate(page=page, per_page=20)

        # If 'user' is not current user, exclude private characters
        else:
            characters = Character.query.order_by(Character.name) \
                .filter_by(user=user, private=False) \
                .paginate(page=page, per_page=20)

    # If 'gender' query parameter exists, only show characters of that
    # gender
    elif gender:
        characters = Character.query.order_by(Character.name) \
            .filter_by(gender=gender, private=False) \
            .paginate(page=page, per_page=20)

    else:
        characters = Character.query.order_by(Character.name) \
            .filter_by(private=False) \
            .paginate(page=page, per_page=20)
    return render_template(
        'all_characters.html',
        characters=characters,
        gender=gender,
        user=user,
        page=page)


@characters.route('/make_private', methods=['POST'])
@login_required
def change_privacy():
    """
    Receive and respond to a POST request by updating a Character's
    privacy setting in the database and sending an appropriate success
    message.

    :return: A success message
    """
    character_id = request.form['id']
    character = Character.query.filter_by(id=character_id).first()
    character.private = not character.private
    db.session.add(character)
    db.session.commit()
    if character.private:
        flash('This character is now private.', 'good')
    else:
        flash('This character is now public.', 'good')
    return 'Privacy settings successfully updated.'


@characters.route('/character/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    """
    Render a template for editing and updating a character, and receive
    POST requests with updated characters.

    :param id: the id of the character to be updated.
    :return: an abort with a 403, a success message, or
    'new_character.html' template with character data.
    """
    character = Character.query.get_or_404(id)

    if current_user != character.user:
        return abort(403)

    # On a post request, update the character with the posted data
    if request.method == 'POST':
        edited_character = request.form
        character.id = id
        character.name = edited_character['name']
        character.gender = edited_character['gender']
        character.height = edited_character['height']
        character.weight = edited_character['weight']
        character.hair_color = edited_character['hair_color']
        character.eye_color = edited_character['eye_color']
        character.unique_attribute = \
            edited_character['unique_attribute']
        character.favorite_clothes = \
            edited_character['favorite_clothes']
        character.hair = edited_character['hair']
        character.mannerism_one = edited_character['mannerism_one']
        character.mannerism_two = edited_character['mannerism_two']
        character.speaking_style = edited_character['speaking_style']
        character.skill = edited_character['skill']
        character.flaw = edited_character['flaw']
        character.fear = edited_character['fear']
        character.favorite = edited_character['favorite']
        character.family = edited_character['family']
        character.friends = edited_character['friends']
        character.significant_other = \
            edited_character['significant_other']
        character.user = current_user
        db.session.commit()
        flash('Your character has been saved!', 'good')

        # The post came from 'static/main.js', and the returned string
        # is a response telling JavaScript that the post was successful
        return 'Character saved successfully.'

    return render_template(
        'new_character.html',
        name=character.name,
        gender=character.gender,
        character=character)


@characters.route('/character/<int:id>/delete', methods=['POST'])
@login_required
def delete(id):
    """
    Receive POST requests for deleting characters.

    :param id: id of the character to be deleted.
    :return: an abort with a 403, or a success message.
    """
    character_id = request.form['id']
    character = Character.query.get_or_404(character_id)

    # Prevent unauthorized users from deleting a character
    if current_user != character.user:
        return abort(403)

    db.session.delete(character)
    db.session.commit()
    flash(f'{character.name} has been deleted.', 'neutral')
    return 'Character deleted successfully.'


@characters.route('/add_favorite/<int:id>')
@login_required
def add_favorite(id):
    """
    Save a character as a favorite character for the current user.

    :param id: Character id.
    :return: an abort with a 403, or a redirect to
    'characters.character' with the Character id.
    """
    character = Character.query.get_or_404(id)

    # Prevent users from adding private characters to favorites
    if character.private:
        return abort(403)

    # Create and commit the new Favorite instance
    favorite = Favorite(user=current_user, character=character)
    db.session.add(favorite)
    db.session.commit()

    flash(f'{character.name} has been added to your Favorites!', 'good')
    return redirect(url_for('characters.character', id=id))

