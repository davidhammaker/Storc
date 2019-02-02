import os
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    api_key = os.environ.get('BTN_KEY')
    gender = 'f'
    random_name_url = f'https://www.behindthename.com/api/random.json' \
        f'?usage=eng&number=1&randomsurname=yes&gender={gender}' \
        f'&key={api_key}'
    names_request = requests.get(random_name_url)
    names_list = names_request.json()['names']
    name = f'Name: {names_list[0]} {names_list[1]}'
    return name


if __name__ == '__main__':
    app.run(debug=True)
