from flask import Flask, url_for
import os
from os import environ


class Config(object):
    pass


class DevelopmentConfig(Config):
    SECRET_KEY = 'secret key'
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///new.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'email'
    MAIL_PASSWORD = 'password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    

class ProductionConfig(Config):
    SECRET_KEY = 'secret key'
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'data base url'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'usename@gmail.com'
    MAIL_PASSWORD = 'password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

