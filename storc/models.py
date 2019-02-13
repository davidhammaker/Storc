from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from storc import app, db


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=False)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    profile_picture = db.Column(db.String)
    about_me = db.Column(db.Text)
    email = db.Column(db.String, unique=True)
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
