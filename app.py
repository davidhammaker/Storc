import os
from random import choice
import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    api_key = os.environ.get('BTN_KEY')
    gender = choice(['male', 'female'])
    random_name_url = f'https://www.behindthename.com/api/random.json' \
        f'?usage=eng&number=1&randomsurname=yes&gender={gender[0]}' \
        f'&key={api_key}'

    # In the future, the next 3 lines will be un-commented:
    # names_request = requests.get(random_name_url)
    # names_list = names_request.json()['names']
    # name = f'Name: {names_list[0]} {names_list[1]}'

    # Temporary name:
    name = 'John Doe'
    return render_template('base.html', name=name,
                           gender=gender.title())


if __name__ == '__main__':
    app.run(debug=True)
