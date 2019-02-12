from datetime import datetime
from storc import db


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
    characters = db.relationship('Character', backref='user', lazy=True)
