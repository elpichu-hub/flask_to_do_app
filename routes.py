
from app import app, db, login_manager, mail
from flask import render_template, redirect, url_for, flash
from forms import SignUp, LogIn, TaskForm, FindYourAccount, ResetCode, ResetPassword

from flask_login import login_required, login_user, logout_user, current_user
from models import User, Task
from flask_mail import Message


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


@app.route('/find-your-account', methods=['POST', 'GET'])
def find_your_account():
    form = FindYourAccount()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            user.reset_code()
            print(type(user.reset_code()))
            msg = Message("Password Recovery Code", sender = app.config['MAIL_USERNAME'], recipients = [form.email.data])
            msg.body = f"You have requested to reset your password. Your recovery code is: {user.reset_code()}"
            mail.send(msg)
            return redirect(url_for('reset_code', username=user.username))
        else:
            flash('There is not account with that email. Please create an account first!', 'warning')
    return render_template('/find-your-account.html', form=form)



@app.route('/reset_code/<username>', methods=['POST', 'GET'])
def reset_code(username):
    form = ResetCode()
    user = User.query.filter_by(username=username).first()
    if form.validate_on_submit():
        if form.reset_code.data == user.password_hash:
            return redirect(url_for('reset_password', username=user.username))
        
    return render_template('/reset_code.html', form=form, user=user)


@app.route('/reset_password/<username>', methods=['POST', 'GET'])
def reset_password(username):
    form = ResetPassword()
    user = User.query.filter_by(username=username).first()
    print(user.username)
    if form.validate_on_submit():
        print('validated')
        user.set_password(form.password.data)
        db.session.commit()
        msg = Message("Password Recovery Code", sender = app.config['MAIL_USERNAME'], recipients = [user.email])
        msg.body = f"Your password has been changed."
        mail.send(msg)
        return redirect(url_for('login'))
    return render_template('/reset_password.html', user=user, form=form)



@app.route('/<username>', methods=['POST', 'GET'])
@login_required
def user(username):
    user = User.query.filter_by(id=current_user.id).first_or_404()
    tasks = Task.query.filter_by(user_id=user.id).order_by('date').all()
    form = TaskForm()
    if form.validate_on_submit():
        try:
            ## this one is the first format i tried, it worked by not optimal##
            #task = Task(date=datetime.strptime(form.date.data, '%m/%d/%y-%I:%M %p'), task_description=form.task_description.data, user_id=user.id)
            task = Task(date=form.date.data, task_description=form.task_description.data, user_id=user.id)
            db.session.add(task)
            db.session.commit()
            flash('Task created!', 'success')
            return redirect(url_for('user', username=user.username))
        except Exception as e:
            flash(f"Something went wrong. Try again!", 'warning')
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


@login_manager.unauthorized_handler
def unauthorized():
    return render_template('unauthorized.html')




@app.route('/guide')
def guide():
    return render_template('guide.html')

@app.route('/about')
def about():
    return render_template('about.html')


