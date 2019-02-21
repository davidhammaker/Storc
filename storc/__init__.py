from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_login import LoginManager
from storc.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()


def create_app(config_class=Config):
    """
    Create a new app instance.

    :param config_class: the application's configuration class.
    :return: the application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)

    from storc.main.views import main
    from storc.users.views import users
    from storc.characters.views import characters
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(characters)

    return app
