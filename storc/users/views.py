import os
import secrets
from flask import (
    flash, redirect, render_template, url_for, request, Blueprint,
    abort)
from flask_login import (
    current_user, login_user, logout_user, login_required)
from PIL import Image
from storc import bcrypt, db
from storc.models import User, Character, Favorite
from storc.forms import (
    EmailRegistrationForm, EmailVerifyForm, EmailLoginForm,
    ResetPasswordForm, EmailSettingsForm, AlternateSettingsForm)
from storc.users.utils import (
    send_verify_email, send_new_email, send_pw_reset_email,
    get_profile_picture, delete_old_picture, upload_profile_picture)


users = Blueprint('users', __name__)


@users.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    """
    Render a form for obtaining information from a new user.

    :return: a redirect that points to 'main.home', or 'sign_up.html'
    template with a form instance.
    """
    form = EmailRegistrationForm()
    if form.validate_on_submit():

        # Hash the user's password before it is stored in the database
        pw_hash = bcrypt.generate_password_hash(
            form.password.data.encode('utf8'))

        user = User(
            username=form.username.data,
            name=form.name.data,
            email=form.email.data,
            password=pw_hash.decode('utf8'),
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
    """
    Render a form to allow users to submit an email address for
    verification. Users may utilize this form if a former token has
    expired.

    :return: a redirect that points to 'main.home' or 'users.sign_up',
    or 'send_verify.html' template with a form instance.
    """

    # Redirect authenticated users to 'main.home'
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = EmailVerifyForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:

            # A validated user does not need email verification
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

        # If the user's email address is not in the database, redirect
        # the user to 'user.sign_up'
        else:
            flash(
                'That email address has not been registered.',
                'neutral')
            return redirect(url_for('users.sign_up'))

    return render_template('send_verify.html', form=form)


@users.route('/verify_email/<token>')
def verify_email(token):
    """
    Validate email verification URL token to verify user email address.

    :param token: the token included in the URL in the verification
    email.
    :return: a redirect pointing to 'users.send_verify_request' or
    'users.email_login'.
    """
    user = User.validate_token(token)

    # If the token is invalid, redirect to 'users.send_verify_request'
    # so that the user may attempt to send the verification URL again.
    if not user:
        flash('That token is invalid.', 'bad')
        return redirect(url_for('users.send_verify_request'))

    # If a user is already validated, redirect to 'users.email_login'
    if user.validated:
        flash(
            'That email address has already been verified!', 'neutral')
        return redirect(url_for('users.email_login'))

    # If a different user is logged in at the time the email is
    # verified, log out that user
    if current_user.is_authenticated:
        logout()

    user.validated = True
    db.session.add(user)
    db.session.commit()
    flash(
        'Your email address has been verified! You may now log in.',
        'good')

    # Redirect to 'users.email_login' so that the user may log in after
    # verification
    return redirect(url_for('users.email_login'))


@users.route('/login/email', methods=('GET', 'POST'))
def email_login():
    """
    Render a form that allows users to log in with an email address.

    :return: a redirect to 'main.home', 'users.send_verify_request', or
    any view function represented by the URL parameter 'next', or
    'email_login.html' template with a form instance.
    """

    # Redirect authenticated users to 'main.home'
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = EmailLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user exists, that the password matches, and
        # that the user's email address has been validated
        if user and bcrypt.check_password_hash(
                user.password, form.password.data.encode('utf8'))\
                and user.validated:
            login_user(user, remember=form.remember_me.data)

            # Remove 'temp_email', if any exists
            user.temp_email = None
            db.session.add(user)
            db.session.commit()

            # Retrieve the view function represented by the parameter
            # 'next' in the URL, if any exists
            next_page = request.args.get('next')

            flash('You have successfully logged in!', 'good')

            # If 'next' existed, redirect to that view function
            if next_page:
                return redirect(url_for(next_page))

            else:
                return redirect(url_for('main.home'))
        elif not user:
            flash(
                'That email address has no matches in our system.',
                'bad')

        # If the email address exists in the database but has not been
        # verified, redirect to 'users.send_verify_request' so that the
        # user may verify the email address and log in
        elif not user.validated:
            flash('That email address has not been verified.', 'bad')
            return redirect(url_for('users.send_verify_request'))

        # If the email address exists but the password does not match,
        # the user either entered the wrong email address or the wrong
        # password
        else:
            flash(
                'Failed to log in. Please check your email and '
                'password.', 'bad')
    return render_template('email_login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    """
    Log out the current user.

    :return: a redirect to 'main.home'.
    """
    logout_user()
    flash('You have logged out.', 'neutral')
    return redirect(url_for('main.home'))


@users.route('/reset_password', methods=['GET', 'POST'])
def reset_password_request():
    """
    Render a form that allows users to receive an email with a URL that
    points to 'users.reset_password', so that users may perform password
    resets.

    :return: 'reset_password_request.html' template with a form
    instance.
    """

    if current_user.is_authenticated:

        # Prevent non-email users from requesting a new password
        if current_user.login != 'email':
            return redirect(url_for('main.home'))

        send_pw_reset_email(current_user)
        flash(
            f'Check your email! We sent a link to '
            f'"{current_user.email}".', 'good')
        return redirect(url_for('users.settings'))

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
    """
    Validate email verification URL token and render a form that allows
    users perform a password reset.

    :param token: the token included in the URL in the password reset
    request email.
    :return: a redirect to 'users.reset_password_request' or
    'users.email_login', or 'reset_password.html' template with a form
    instance.
    """
    user = User.validate_token(token)

    # If the token is invalid, redirect to
    # 'users.reset_password_request' so that the user may attempt to
    # send the reset password URL again.
    if not user:
        flash('That token is invalid.', 'bad')
        return redirect(url_for('users.reset_password_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():

        # Note whether the user was logged in, then log out
        was_logged_in = False
        if current_user.is_authenticated:
            was_logged_in = True
            logout_user()
            flash('You have logged out.', 'neutral')

        # Hash the user's password before it is stored in the database
        pw_hash = bcrypt.generate_password_hash(
            form.password.data.encode('utf8'))

        user.password = pw_hash.decode('utf8')
        db.session.add(user)
        db.session.commit()
        flash(
            'Your password has been reset! You may now log in.',
            'good')

        # If the user was logged in, redirect to 'users.settings' after
        # logging in
        if was_logged_in:
            return redirect(
                url_for('users.email_login', next='users.settings'))

        return redirect(url_for('users.email_login'))
    return render_template('reset_password.html', form=form)


@users.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    """
    Render a form that allows users to update account settings.

    :return: 'settings.html' template with a form instance and a URL
    path for the current user's profile picture.
    """

    # Provide users with the correct form
    if current_user.login == 'email':
        form = EmailSettingsForm()
    else:
        form = AlternateSettingsForm()

    if form.validate_on_submit():
        user = current_user

        # Prepare a message
        message = None

        # If the user's name, username, or profile picture is updated,
        # save the changes to the database
        if current_user.login == 'email':
            if form.name.data != user.name:
                user.name = form.name.data
                db.session.add(user)
                db.session.commit()
                message = 'Changes have been saved!'
        if (
                form.username.data != user.username) or (
                form.profile_picture.data):
            message = 'Changes have been saved!'

            # Start by saving name and/or username

            if form.username.data != user.username:
                user.username = form.username.data
                db.session.add(user)
                db.session.commit()

            # Check whether the profile picture has been updated, and
            # update it if necessary
            if form.profile_picture.data:
                _, extension = os.path.splitext(
                    form.profile_picture.data.filename)

                # If the user's old profile picture was not the default
                # profile picture, delete it
                old_picture = None
                if user.profile_picture != 'default.jpg':
                    old_picture = user.profile_picture
                if old_picture:
                    delete_old_picture(old_picture)

                # Save the filename of the profile picture as a random
                # hex with the correct file extension
                user.profile_picture = \
                    f'{secrets.token_hex(8)}{extension}'
                db.session.add(user)
                db.session.commit()

                # Resize the image's dimensions so that height and width
                # are 200px maximum
                size = (200, 200)
                i = Image.open(form.profile_picture.data)
                i.thumbnail(size)

                # If the resized image is not a perfect 200x200 square,
                # paste the image onto a black 200x200 square background
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

                # Temporarily save the image in the working directory,
                # then read the image in binary from the directory
                final_image.save(f'{user.profile_picture}')
                data = open(f'{user.profile_picture}', 'rb').read()

                # Upload the binary data and the filename to Dropbox
                upload_profile_picture(data, user.profile_picture)

                # Delete the image stored in the working directory
                os.remove(f'{user.profile_picture}')

        if message:
            flash(message, 'good')

        # If the email address has been updated, store the new email
        # address as 'temp_email' until verification, and send an email
        # to the new address for verification
        if current_user.login == 'email':
            if form.email.data != user.email:
                user.temp_email = form.email.data
                db.session.add(user)
                db.session.commit()
                send_new_email(user)
                flash(
                    f'An email has been sent to "{user.temp_email}". '
                    f'Check your email to verify the change!', 'good')

    image_path = get_profile_picture(current_user)
    return render_template(
        'settings.html', form=form, image_path=image_path)


@users.route('/new_email/<token>')
def new_email(token):
    """
    Validate email verification URL token to verify a user's new email
    address.

    :param token: the token included in the URL in the verification
    email.
    :return: a redirect to 'users.settings' or 'users.email_login'.
    """
    user = User.validate_token(token)
    if not user:
        flash('That token is invalid.', 'bad')
    else:

        # Prevent users from setting 'email' to 'None', since
        # 'temp_email' becomes 'None' after a successful login
        if not user.temp_email:
            flash('Your new email address could not be verified. '
                  'Please try again.', 'bad')
            return redirect(url_for('users.settings'))

        user.email = user.temp_email
        user.temp_email = None
        db.session.add(user)
        db.session.commit()
        flash('Your new email address has been verified!', 'good')
    return redirect(url_for('users.email_login'))


@users.route('/<string:username>')
def profile(username):
    """
    Render a template displaying information about a user.

    :param username: the user's username.
    :return: an abort with a 404 or 'profile.html' template with
    relevant user details.
    """
    user = User.query.filter_by(username=username).first()

    # If no user exists, abort 404
    if not user:
        return abort(404)

    # Get the user's profile picture
    image_path = get_profile_picture(user)

    # Display private characters if the user is also the current user
    if user == current_user:
        recent_characters = \
            Character.query.filter_by(user=user)\
            .order_by(Character.date.desc()).limit(5)

    # If the current user is not the user, don't display private
    # characters
    else:
        recent_characters = \
            Character.query.filter_by(user=user, private=False)\
            .order_by(Character.date.desc()).limit(5)

    # Get the user's favorite characters
    favorites_raw = Favorite.query.filter_by(user=user)\
        .order_by(Favorite.date.desc()).limit(5)

    # If the current user is not the user, don't display private
    # characters among the favorites
    favorites = []
    if user != current_user:
        for favorite in favorites_raw:
            character = Character.query.get(favorite.character_id)
            if not character.private:
                favorites.append(character)

    # If the current user is the user, include private characters
    else:
        for favorite in favorites_raw:
            character = Character.query.get(favorite.character_id)
            favorites.append(character)

    return render_template(
        'profile.html',
        user=user,
        image_path=image_path,
        recent_characters=recent_characters,
        favorites=favorites)
