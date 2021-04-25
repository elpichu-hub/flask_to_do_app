from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, TextAreaField, DateField, DateTimeField, TimeField
from wtforms.validators import DataRequired, EqualTo, Email, Length, Required




class SignUp(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=5, max=100, message='Username must be min 5 characters!')])
    email = StringField('email', validators=[DataRequired(message='Invalid Email'), Email()])
    password = PasswordField('password', validators=[DataRequired(), validators.Length(min=6, max=10, message='Password must be between 6 and 10 characters long.')])
    password1 = PasswordField('Re-enter password', validators=[ DataRequired(), EqualTo('password', message='Password fields must match. Try again!')])
    submit = SubmitField('submit')


class LogIn(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


class TaskForm(FlaskForm):
    date = StringField('Date', validators=[DataRequired(message='You must enter a date!')])
    task_description = StringField('Task Description', validators=[DataRequired(), Length(min=5, max=100, message='Task description must be at least 5 characters long!')])
    create_task = SubmitField('Create Task')

    







    