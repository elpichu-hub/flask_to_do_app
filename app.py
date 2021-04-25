from flask import Flask, current_app, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore







app = Flask(__name__)

scheduler = BackgroundScheduler()
scheduler.add_jobstore('sqlalchemy', url='sqlite:///new.db')


login_manager = LoginManager()
login_manager.init_app(app)


if app.config['ENV'] == 'development':
    app.config.from_object('config.DevelopmentConfig')
else:
    app.config.from_object('config.ProductionConfig')






mail = Mail(app)
mail_test = Mail(app)




db = SQLAlchemy(app)




import routes






