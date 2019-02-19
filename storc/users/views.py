import os
import secrets
from flask import (
    flash, redirect, render_template, url_for, request, Blueprint)
from flask_login import (
    current_user, login_user, logout_user, login_required)
from PIL import Image
from storc import bcrypt, db
from storc.models import User
from storc.forms import (
    EmailRegistrationForm, EmailVerifyForm, EmailLoginForm,
    ResetPasswordForm, SettingsForm)
from storc.users.utils import (
    send_verify_email, send_new_email, send_pw_reset_email,
    get_profile_picture, delete_old_picture, upload_profile_picture)


users = Blueprint('users', __name__)


@users.route('/sign_up', methods=['GET', 'POST'])
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
        return redirect(url_for('main.home'))
    return render_template('sign_up.html', form=form)


@users.route('/verify_email', methods=['GET', 'POST'])
def send_verify_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = EmailVerifyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.validated:
                flash(
                    'That email address has already been verified!',
                    'neutral')
                return redirect(url_for('main.home'))
            send_verify_email(user)
            flash(
                f'Check your email! We sent a verification link to '
                f'"{form.email.data}".', 'good')
            return redirect(url_for('main.home'))
        else:
            flash(
                'That email address has not been registered.',
                'neutral')
            return redirect(url_for('users.sign_up'))
    return render_template('send_verify.html', form=form)


@users.route('/verify_email/<token>')
def verify_email(token):
    user = User.validate_token(token)
    if not user:
        flash('That token is invalid.', 'bad')
        return redirect(url_for('users.send_verify_request'))
    if current_user.is_authenticated:
        logout()
    user.validated = True
    db.session.add(user)
    db.session.commit()
    flash(
        'Your email address has been verified! You may now log in.',
        'good')
    return redirect(url_for('users.email_login'))


@users.route('/email_login', methods=('GET', 'POST'))
def email_login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
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
                return redirect(url_for('main.home'))
        elif not user:
            flash(
                'That email address has no matches in our system.',
                'bad')
        elif not user.validated:
            flash('That email address has not been verified.', 'bad')
            return redirect(url_for('users.send_verify_request'))
        else:
            flash(
                'Failed to log in. Please check your email and '
                'password.', 'bad')
    return render_template('login.html', form=form)


@users.route('/logout')
def logout():
    logout_user()
    flash('You have logged out.', 'neutral')
    return redirect(url_for('main.home'))


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
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


@users.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.validate_token(token)
    if not user:
        flash('That token is invalid.', 'bad')
        return redirect(url_for('users.reset_password_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        pw_hash = bcrypt.generate_password_hash(form.password.data)
        user.password = pw_hash
        db.session.add(user)
        db.session.commit()
        flash(
            'Your password has been reset! You may now log in.',
            'good')
        return redirect(url_for('users.email_login'))
    return render_template('reset_password.html', form=form)


@users.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm()
    image_path = get_profile_picture(current_user)
    if form.validate_on_submit():
        user = current_user
        if (
                form.name.data != user.name) or (
                form.username.data != user.username) or (
                form.profile_picture.data):
            message = 'Changes have been saved!'
            if form.name.data != user.name:
                user.name = form.name.data
            if form.username.data != user.username:
                user.username = form.username.data
            db.session.add(user)
            db.session.commit()
            if form.profile_picture.data:
                _, extension = os.path.splitext(
                    form.profile_picture.data.filename)
                old_picture = None
                if user.profile_picture != 'default.jpg':
                    old_picture = user.profile_picture
                user.profile_picture = \
                    f'{secrets.token_hex(8)}{extension}'
                db.session.add(user)
                db.session.commit()
                size = (200, 200)
                i = Image.open(form.profile_picture.data)
                i.thumbnail(size)
                if i.height != 200 and i.width != 200:
                    background = Image.open(
                        'storc/static/profile_background.jpg')
                    distance_h = (200 - i.height) // 2
                    distance_w = (200 - i.width) // 2
                    background.paste(i, (distance_w, distance_h))
                    final_image = background
                elif i.height != 200:
                    background = Image.open(
                        'storc/static/profile_background.jpg')
                    distance = (200 - i.height) // 2
                    background.paste(i, (0, distance))
                    final_image = background
                elif i.width != 200:
                    background = Image.open(
                        'storc/static/profile_background.jpg')
                    distance = (200 - i.width) // 2
                    background.paste(i, (distance, 0))
                    final_image = background
                else:
                    final_image = i
                final_image.save(f'{user.profile_picture}')
                data = open(f'{user.profile_picture}', 'rb').read()
                if old_picture:
                    delete_old_picture(old_picture)
                upload_profile_picture(data, user.profile_picture)
                os.remove(f'{user.profile_picture}')
                message = (
                    'Changes have been saved! Your new profile picture '
                    'will be ready soon.')
            flash(message, 'good')
        if form.email.data != user.email:
            user.temp_email = form.email.data
            db.session.add(user)
            db.session.commit()
            send_new_email(user)
            flash(
                f'An email has been sent to "{user.temp_email}". '
                f'Check your email to verify the change!', 'good')
    return render_template(
        'settings.html', form=form, image_path=image_path)


@users.route('/new_email/<token>')
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
    return redirect(url_for('users.email_login'))
