import os
import requests
from random import choice
from flask import render_template
from storc import app


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
