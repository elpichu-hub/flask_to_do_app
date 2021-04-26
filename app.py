from flask import Flask, current_app, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore




url='postgresql://quwmbantdzhpao:877234c1f72fd64bc78717fbc0f1d833e5c1e2c7e98af612e67badef983ad03a@ec2-34-225-167-77.compute-1.amazonaws.com:5432/d4mlir0vcgc3ho'
url1 = 'sqlite:///new.db'

app = Flask(__name__)



jobstores = {
    'sqlalchemy': SQLAlchemyJobStore(url=url1)
}

scheduler = BackgroundScheduler()


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






