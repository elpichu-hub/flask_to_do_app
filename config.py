from flask import Flask, url_for
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
    SQLALCHEMY_DATABASE_URI = 'postgresql://quwmbantdzhpao:877234c1f72fd64bc78717fbc0f1d833e5c1e2c7e98af612e67badef983ad03a@ec2-34-225-167-77.compute-1.amazonaws.com:5432/d4mlir0vcgc3ho'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'etubrute56@gmail.com'
    MAIL_PASSWORD = 'compay2nd'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

