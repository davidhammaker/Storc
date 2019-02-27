from datetime import datetime
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from flask_dance.consumer.backend.sqla import OAuthConsumerMixin
from storc import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Character(db.Model):
    """The Character model for the SQLAlchemy database."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    height = db.Column(db.String, nullable=False)
    weight = db.Column(db.String, nullable=False)
    hair_color = db.Column(db.String, nullable=False)
    eye_color = db.Column(db.String, nullable=False)
    unique_attribute = db.Column(db.String, nullable=False)
    favorite_clothes = db.Column(db.String, nullable=False)
    hair = db.Column(db.String, nullable=False)
    mannerism_one = db.Column(db.String, nullable=False)
    mannerism_two = db.Column(db.String, nullable=False)
    speaking_style = db.Column(db.String, nullable=False)
    skill = db.Column(db.String, nullable=False)
    flaw = db.Column(db.String, nullable=False)
    fear = db.Column(db.String, nullable=False)
    favorite = db.Column(db.String, nullable=False)
    family = db.Column(db.String, nullable=False)
    friends = db.Column(db.String, nullable=False)
    significant_other = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    private = db.Column(db.Boolean, default=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False)

    def __repr__(self):
        """Character representation."""
        return f"Character(id={self.id}, name={self.name}, " \
            f"date={self.date}, user_id={self.user_id})"


class User(db.Model, UserMixin):
    """The User model for the SQLAlchemy database."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    profile_picture = db.Column(db.String, default='default.jpg')
    about_me = db.Column(db.Text)
    email = db.Column(db.String, unique=True)
    temp_email = db.Column(db.String, default=None)
    password = db.Column(db.String)
    validated = db.Column(db.Boolean)
    login = db.Column(db.String, default='email')
    characters = db.relationship('Character', backref='user', lazy=True)

    def __repr__(self):
        """User representation."""
        return f"User(id={self.id}, username={self.username}, " \
            f"email={self.email}, validated={self.validated})"

    def get_token(self, expire=1800):
        """
        Create a token for the user for verification and security
        purposes.

        :param expire: time in seconds until the token expires.
        :return: serialized token specific to the user.
        """
        s = Serializer(current_app.config['SECRET_KEY'], expire)
        return s.dumps({'user_id': self.id})

    @staticmethod
    def validate_token(token):
        """
        Validate user token.

        :param token: the token to be validated.
        :return: None or a user.
        """
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


class OAuth(OAuthConsumerMixin, db.Model):
    """
    The OAuth model for storing provider information and Oauth tokens.
    """
    provider_user_id = db.Column(db.String(256), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User)
