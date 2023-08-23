from app import app, db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
import secrets


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=False, index=True)
    email = db.Column(db.String(50), unique=True, index=True)
    password_hash = db.Column(db.String(100))
    tasks = db.relationship('Task', backref='user', lazy='dynamic', cascade='delete, all, delete-orphan')

    def __repr__(self):
        return f'{self.email}'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def reset_code(self):
        self.password_hash = secrets.token_urlsafe(8)
        db.session.commit()
        return self.password_hash
        

    
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime())
    task_description = db.Column(db.String(50), unique=False, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.task_description}'


