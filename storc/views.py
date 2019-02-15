import os
import requests
from random import choice
from flask import render_template, request, flash, redirect, url_for
from flask_mail import Message
from flask_login import login_user, logout_user
from storc import app, db, bcrypt, mail
from storc.forms import (
    EmailRegistrationForm, EmailVerifyForm, EmailLoginForm)
from storc.models import User


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
    # TODO: Insert redirect for authenticated users.
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
    # TODO: Insert redirect for authenticated users.
    user = User.validate_token(token)
    if not user:
        flash('That token is invalid.', 'bad')
        return redirect(url_for('send_verify_request'))
    user.validated = True
    db.session.add(user)
    db.session.commit()
    flash(
        'Your email address has been validated! You may now log in.',
        'good')
    return redirect(url_for('home'))


@app.route('/email_login', methods=('GET', 'POST'))
def email_login():
    # TODO: Insert redirect for authenticated users.
    form = EmailLoginForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, form.password.data) and user.validated:
            login_user(user, remember=form.remember_me.data)
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
