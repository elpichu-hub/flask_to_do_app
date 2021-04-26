from myfilters import laz
from app import app, db, login_manager, mail, mail_test, scheduler
from flask import Flask, render_template, redirect, url_for, request, flash
from forms import SignUp, LogIn, TaskForm
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models import User, Task
from flask_mail import Mail, Message
from datetime import datetime, date
import os




date = datetime.now()

def task_date_check():
    with app.app_context():
        tasks = Task.query.all()
        for task in tasks:
            if task.date.date() == date.date():
                user = User.query.get(task.user_id)
                msg = Message(f"Hi, {user.username}. This is a reminder.", sender=app.config['MAIL_USERNAME'], recipients=[user.email])
                msg.body = f"{user.username}, your task '{task.task_description}' is scheduled for today: {date.date()} at {task.date.time()}. Please remove task from app to stop receiving emails about this task."
                mail_test.send(msg)


###testting the scheduler 
def printing():
    with app.app_context():
        date = datetime.now().second
        print(date)
        
           


if not app.debug or os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    check_hour_job = scheduler.add_job(task_date_check, 'interval', minutes=120, id='myjob', replace_existing=True)  
    scheduler.start()
    scheduler.print_jobs()








@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def home():
    form = SignUp()
    if current_user.is_authenticated:
        return redirect(url_for('user', username=current_user.username))
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() == None:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            try:
                db.session.commit()
                flash('Account created!', 'success')
                msg = Message("Mexican Joker", sender = 'lazlemlop@gmail.com', recipients = [form.email.data])
                msg.body = "Women belong in the kitchen!"
                mail.send(msg)
            except Exception as e:
                print(e)
                db.session.rollback()
        else:
            flash('Email is already in use!', 'warning')
    return render_template('home.html', form=form)




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LogIn()
    if current_user.is_authenticated:
        return redirect(url_for('user', username=current_user.username))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            print('user logged in!')
            return redirect(url_for('user', username=user.username))
        else:
            flash('Invalid email or password. Try again!', 'warning')
    return render_template('login.html', form=form)




@app.route('/<username>', methods=['POST', 'GET'])
@login_required
def user(username):
    user = User.query.filter_by(id=current_user.id).first_or_404()
    tasks = Task.query.filter_by(user_id=user.id).order_by('date').all()
    form = TaskForm()
    
    if form.validate_on_submit():
        try:
            task = Task(date=datetime.strptime(form.date.data, '%m/%d/%y-%I:%M %p'), task_description=form.task_description.data, user_id=user.id)
            db.session.add(task)
            db.session.commit()
            flash('Task created!', 'success')
            return redirect(url_for('user', username=user.username))
        except Exception as e:
            flash(f"Date and Time format is MM/DD/YY-HH:MM AM", 'warning')
            return redirect(url_for('user', username=user.username))
    
    return render_template('user.html', user=user, form=form, tasks=tasks)











@app.route('/delete/<int:id>')
def delete(id):
    remove = Task.query.get_or_404(id)
    db.session.delete(remove)
    db.session.commit()
    return redirect(url_for('user', username=current_user.username))



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404



@app.route('/logout')
@login_required
def logout():
    logout_user()
    print('user logged out')
    return redirect('home')



@app.route('/school')
def school():
    return render_template('school.html')



@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html')




@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/about')
def about():
    return render_template('about.html')


