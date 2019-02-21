import os


class Config:
    """The application's configuration class."""
    SQLALCHEMY_DATABASE_URI = os.environ.get('STORC_DB')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('STORC_SECRET')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('STORC_EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('STORC_EMAIL_PASS')
