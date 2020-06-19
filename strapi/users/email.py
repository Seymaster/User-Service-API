# from flask.ext.mail import Message
from flask_mail import Message
from strapi import app, mail

def send_email(to, subject,template):
    msg = Message(
        subject,
        recipients = [to],
        html = template
    )
    mail.send(msg)