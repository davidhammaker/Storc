import os
from random import choice
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    gender = choice(['male', 'female'])

    # The following lines have been commented out for development:
    # api_key = os.environ.get('BTN_KEY')
    # random_name_url = f'https://www.behindthename.com/api/random.json' \
    #     f'?usage=eng&number=1&randomsurname=yes&gender={gender[0]}' \
    #     f'&key={api_key}'
    # names_request = requests.get(random_name_url)
    # names_list = names_request.json()['names']
    # name = f'Name: {names_list[0]} {names_list[1]}'

    # Temporary name for development:
    name = 'John Doe'
    return render_template('base.html', name=name,
                           gender=gender.title())


if __name__ == '__main__':
    app.run(debug=True)
