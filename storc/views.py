import os
import requests
from random import choice
from flask import render_template, request, flash, redirect, url_for
from storc import app, db, bcrypt
from storc.forms import EmailRegistrationForm
from storc.models import User


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/new_character')
def new_character():
    gender = choice(['male', 'female'])

    # The following lines have been commented out for development:
    # api_key = os.environ.get('BTN_KEY')
    # random_name_url = f'https://www.behindthename.com/api/random.json' \
    #     f'?usage=eng&number=1&randomsurname=yes&gender={gender[0]}' \
    #     f'&key={api_key}'
    # names_request = requests.get(random_name_url)
    # names_list = names_request.json()['names']
    # name = f'{names_list[0]} {names_list[1]}'

    # Temporary name for development:
    name = 'John Doe'
    return render_template('new_character.html', name=name,
                           gender=gender.title())


@app.route('/save_character', methods=['POST'])
def save_character():
    character = request.form
    character_data = {key: character[key] for key in character.keys()}
    return 'Character Data Received'


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = EmailRegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            name=form.name.data,
            email=form.email.data,
            password=pw_hash)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('sign_up.html', form=form)
