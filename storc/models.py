from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from storc import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    private = db.Column(db.Boolean, default=False)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    profile_picture = db.Column(db.String, default='default.jpg')
    about_me = db.Column(db.Text)
    email = db.Column(db.String, unique=True)
    temp_email = db.Column(db.String, default=None)
    password = db.Column(db.String)
    validated = db.Column(db.Boolean)
    characters = db.relationship('Character', backref='user', lazy=True)

    def get_token(self, expire=1800):
        s = Serializer(app.config['SECRET_KEY'], expire)
        return s.dumps({'user_id': self.id})

    @staticmethod
    def validate_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
