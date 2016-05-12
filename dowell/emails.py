from flask.ext.mail import Message
from dowell import mail
from .decorators import async
from dowell import app
from flask import render_template
from config import ADMINS
from threading import Thread

@async
def send_async_email(app, mail_message):
    with app.app_context():
        mail.send(mail_message)
		
def send_email(subject, sender, recipients, text_body):
    mail_message = Message(subject, sender=sender, recipients=recipients)
    mail_message.body = text_body
    send_async_email(app, mail_message)
	
def task_reminder(rem_data, event, reciever):
	if event == 'signup':
		mailtype = 'welcome.txt'
		mail_subject = "Welcome to DoWell"
	else:
		mailtype = 'reminder_email.txt'
		mail_subject = "[DoWell] Task Reminder for %s " % rem_data[1]
	send_email(mail_subject, ADMINS[0], [reciever], render_template(mailtype, rem_data = rem_data))