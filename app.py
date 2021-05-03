from flask import Flask, current_app, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message





app = Flask(__name__)





login_manager = LoginManager()
login_manager.init_app(app)


if app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.ProductionConfig')






mail = Mail(app)
mail2 = Mail(app)





db = SQLAlchemy(app)





import routes






