
class Config(object):
    pass

class DevelopmentConfig(Config):
    SECRET_KEY = 'dev'
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///new.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'etubrute56@gmail.com'
    MAIL_PASSWORD = 'prsxyqoxhlodlpis'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    

class ProductionConfig(Config):
    SECRET_KEY = 'prod'
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///new.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'usename@gmail.com'
    MAIL_PASSWORD = 'password'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

