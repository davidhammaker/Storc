# Storc | Character Generator

A random character generator that creates a named character to inspire your creativity.

## Purpose

This tool is intended for anyone who is struggling to come up with unique characters, with names and other qualities, for a work of literature or other creative work.

## Dependencies

Requires Python 3.6 or higher to work properly.

Requires the installation of all packages listed in `requirements.txt`.

Requires that the following environment variables be set appropriately:
* "STORC_DB" (Should be a database URI. See [here](http://flask-sqlalchemy.pocoo.org/2.3/quickstart/).)
* "STORC_SECRET" (Should be a random hash or complex string.)
* "STORC_EMAIL_USER"***** (The email address from which the application sends emails.)
* "STORC_EMAIL_PASS"***** (The password for the email address.)
* "BTN_KEY"****** (The API key for Behind the Name)
* "STORC_DROPBOX_KEY"******* (The API key for Dropbox)

***** Depending on the domain of the email address you use, you may be prevented from allowing the application to log in. This is the case with Gmail, for example, which prevents "less secure applications" from gaining access to its accounts by default. If the email provider you use is blocking "less secure applications", you will have to go into account settings to grant access.

****** Character names are fetched from the [Behind the Name](https://www.behindthename.com/) API. To use this API, you must first set the environment variable "BTN_KEY" to your Behind the Name API key. To obtain an API key, follow the instructions found on the Behind the Name website, [here](https://www.behindthename.com/api/).

******* Profile pictures are saved to a [Dropbox](https://www.dropbox.com) account, including "default.jpg", which is given to all new users who sign up with email. For this functionality to work properly, you will need a Dropbox account and a corresponding API key. View [the documentation](https://dropbox.github.io/dropbox-api-v2-explorer/) for more information.
* After establishing a Dropbox account, you will need to create a default profile picture called "default.jpg" and upload it to Dropbox. An image that is 200x200 pixels will be consistent with the rest of the application.

## Usage

_When using this tool, please be aware that the tool is not yet complete._

To use the application, start by cloning this repository. Use `$ pip install -r requirements.txt` to install all necessary requirements.

If you are running the application for the first time, run `$ python run.py --setup`. Otherwise, you can run the application with `$ python run.py`. You can then view the application at [localhost:5000](http://localhost:5000/).

## Copyright

© 2018-2019 David J. Hammaker
