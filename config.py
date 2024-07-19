
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gu35S-wh4t-1dk'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

     # Flask-Mail configuration
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'd4e8e86e391c87'
    MAIL_PASSWORD = 'c6aafbafc549ec'
    MAIL_DEFAULT_SENDER = 'romeo.test@gmail.com'
    
    ADMINS = ['you@example.com']
    