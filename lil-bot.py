from app import app, mail2, db
from models import User, Task
from flask_mail import Message, Mail
from datetime import datetime



date = datetime.now()


with app.app_context():
    tasks = Task.query.all()
    print(tasks)
    for task in tasks:
        print(task.date.date())
        print(date)
        if task.date.date() == date.date():
            user = User.query.get(task.user_id)
            msg = Message(f"Hi, {user.username}.", sender=app.config['MAIL_USERNAME'], recipients=[User.query.get(task.user_id).email])
            msg.body = f"Your task '{task.task_description}' is scheduled for {task.date}"
            mail2.send(msg)
           