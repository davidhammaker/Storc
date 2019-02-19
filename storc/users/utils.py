import os
import json
import requests
from flask import url_for
from flask_mail import Message
from storc import mail


def send_verify_email(user):
    token = user.get_token()
    message = Message(
        'Verify Your Email',
        sender='storcwebsite@gmail.com',
        recipients=[user.email])
    message.body = f"Thanks for signing up with Storc!\n\nTo verify " \
        f"your email address, please click the link below:\n\n" \
        f"{url_for('users.verify_email', token=token, _external=True)}"
    mail.send(message)


def send_pw_reset_email(user):
    token = user.get_token()
    message = Message(
        'Reset Your Password',
        sender='storcwebsite@gmail.com',
        recipients=[user.email])
    message.body = f"To verify reset your password, click the link " \
        f"below:\n\n" \
        f"{url_for('users.reset_password', token=token, _external=True)}"
    mail.send(message)


def send_new_email(user):
    token = user.get_token()
    message = Message(
        'Verify Your New Email',
        sender='storcwebsite@gmail.com',
        recipients=[user.temp_email])
    message.body = f"The email address associated with your Storc " \
        f"account has changed.\n\nTo verify your new email address, " \
        f"please click the link below:\n\n" \
        f"{url_for('users.new_email', token=token, _external=True)}"
    mail.send(message)


def get_profile_picture(user):
    url = "https://api.dropboxapi.com/2/files/get_temporary_link"
    key = os.environ.get('STORC_DROPBOX_KEY')
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"}
    data = {"path": f"/{user.profile_picture}"}
    response = requests.post(
        url, headers=headers, data=json.dumps(data))
    return response.json()['link']


def delete_old_picture(old_picture):
    url = "https://api.dropboxapi.com/2/files/delete_v2"
    key = os.environ.get('STORC_DROPBOX_KEY')
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"}
    data = {"path": f"/{old_picture}"}
    response = requests.post(
        url, headers=headers, data=json.dumps(data))
    return response.json()


def upload_profile_picture(data, filename):
    url = "https://content.dropboxapi.com/2/files/upload"
    key = os.environ.get('STORC_DROPBOX_KEY')
    dropbox_api_arg = "{\"path\":\"/" + f'{filename}' + "\"}"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": dropbox_api_arg}
    response = requests.post(url, headers=headers, data=data)
    return response.json()
