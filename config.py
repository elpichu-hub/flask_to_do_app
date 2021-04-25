import os
from os import environ


class Config(object):
    pass


class DevelopmentConfig(Config):
    SECRET_KEY = 'Bj97zUiLgVPDR07RMXYP'
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///new.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'etubrute56@gmail.com'
    MAIL_PASSWORD = 'compay2nd'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

class ProductionConfig(Config):
    SECRET_KEY = 'Bj97zUiLgVPDR07RMXYP'
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL1')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'etubrute56@gmail.com'
    MAIL_PASSWORD = 'compay2nd'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

