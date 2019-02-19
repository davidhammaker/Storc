import os
import requests
import json
import secrets
from random import choice
from flask import render_template, request, flash, redirect, url_for
from flask_mail import Message
from flask_login import (
    login_user, logout_user, current_user, login_required)
from PIL import Image
from storc import app, db, bcrypt, mail
from storc.forms import (
    EmailRegistrationForm, EmailVerifyForm, EmailLoginForm,
    ResetPasswordForm, SettingsForm)
from storc.models import User, Character


def send_verify_email(user):
    token = user.get_token()
    message = Message(
        'Verify Your Email',
        sender='storcwebsite@gmail.com',
        recipients=[user.email])
    message.body = f"Thanks for signing up with Storc!\n\nTo verify " \
        f"your email address, please click the link below:\n\n" \
        f"{url_for('verify_email', token=token, _external=True)}"
    mail.send(message)


def send_pw_reset_email(user):
    token = user.get_token()
    message = Message(
        'Reset Your Password',
        sender='storcwebsite@gmail.com',
        recipients=[user.email])
    message.body = f"To verify reset your password, click the link " \
        f"below:\n\n" \
        f"{url_for('reset_password', token=token, _external=True)}"
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
        f"{url_for('new_email', token=token, _external=True)}"
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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/new_character')
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


@app.route('/save_character', methods=['POST'])
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


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = EmailRegistrationForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User(
            username=form.username.data,
            name=form.name.data,
            email=form.email.data,
            password=pw_hash,
            validated=False)
        db.session.add(user)
        db.session.commit()
        send_verify_email(user)
        flash(
            f'Check your email! We sent a verification link to '
            f'"{form.email.data}".', 'good')
        return redirect(url_for('home'))
    return render_template('sign_up.html', form=form)


@app.route('/verify_email', methods=['GET', 'POST'])
def send_verify_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmailVerifyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.validated:
                flash(
                    'That email address has already been verified!',
                    'neutral')
                return redirect(url_for('home'))
            send_verify_email(user)
            flash(
                f'Check your email! We sent a verification link to '
                f'"{form.email.data}".', 'good')
            return redirect(url_for('home'))
        else:
            flash(
                'That email address has not been registered.',
                'neutral')
            return redirect(url_for('sign_up'))
    return render_template('send_verify.html', form=form)


@app.route('/verify_email/<token>')
def verify_email(token):
    user = User.validate_token(token)
    if not user:
        flash('That token is invalid.', 'bad')
        return redirect(url_for('send_verify_request'))
    if current_user.is_authenticated:
        logout()
    user.validated = True
    db.session.add(user)
    db.session.commit()
    flash(
        'Your email address has been verified! You may now log in.',
        'good')
    return redirect(url_for('email_login'))


@app.route('/email_login', methods=('GET', 'POST'))
def email_login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmailLoginForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, form.password.data) and user.validated:
            login_user(user, remember=form.remember_me.data)

            # Remove temp_email, if any exists.
            user.temp_email = None
            db.session.add(user)
            db.session.commit()

            next_page = request.args.get('next')
            flash('You have successfully logged in!', 'good')
            if next_page:
                return redirect(url_for(next_page))
            else:
                return redirect(url_for('home'))
        elif not user:
            flash(
                'That email address has no matches in our system.',
                'bad')
        elif not user.validated:
            flash('That email address has not been verified.', 'bad')
            return redirect(url_for('send_verify_request'))
        else:
            flash(
                'Failed to log in. Please check your email and '
                'password.', 'bad')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You have logged out.', 'neutral')
    return redirect(url_for('home'))


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = EmailVerifyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_pw_reset_email(user)
            flash(
                f'Check your email! We sent a link to '
                f'"{form.email.data}".', 'good')
        else:
            flash(
                'That email address has no matches in our system.',
                'bad')
    return render_template('reset_password_request.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.validate_token(token)
    if not user:
        flash('That token is invalid.', 'bad')
        return redirect(url_for('reset_password_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user.password = pw_hash
        db.session.add(user)
        db.session.commit()
        flash(
            'Your password has been reset! You may now log in.',
            'good')
        return redirect(url_for('email_login'))
    return render_template('reset_password.html', form=form)


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm()
    image_path = get_profile_picture(current_user)
    if form.validate_on_submit():
        user = current_user
        if (form.name.data != user.name) or (
                form.username.data != user.username):
            if form.name.data != user.name:
                user.name = form.name.data
            if form.username.data != user.username:
                user.username = form.username.data
            db.session.add(user)
            db.session.commit()
            flash('Changes have been saved.', 'good')
        if form.email.data != user.email:
            user.temp_email = form.email.data
            db.session.add(user)
            db.session.commit()
            send_new_email(user)
            flash(
                f'An email has been sent to "{user.temp_email}". '
                f'Check your email to verify the change!', 'good')
        if form.profile_picture.data:
            data = form.profile_picture.data.stream.read()
            _, extension = os.path.splitext(
                form.profile_picture.data.filename)
            old_picture = None
            if user.profile_picture != 'default.jpg':
                old_picture = user.profile_picture
            user.profile_picture = f'{secrets.token_hex(8)}{extension}'
            db.session.add(user)
            db.session.commit()
            if old_picture:
                delete_old_picture(old_picture)
            upload_profile_picture(data, user.profile_picture)
    return render_template(
        'settings.html', form=form, image_path=image_path)


@app.route('/new_email/<token>')
def new_email(token):
    user = User.validate_token(token)
    if not user:
        flash('That token is invalid.', 'bad')
    else:
        user.email = user.temp_email
        user.temp_email = None
        db.session.add(user)
        db.session.commit()
        flash('Your new email address has been verified!', 'good')
    return redirect(url_for('email_login'))
