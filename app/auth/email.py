from flask_mail import Message
from app import mail
from flask import render_template, current_app

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    msg = Message('[YourApp] Reset Your Password',
                  sender=current_app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[user.email])
    msg.body = render_template('auth/email_template/reset_password.txt', user=user, token=token)
    msg.html = render_template('auth/email_template/reset_password.html', user=user, token=token)
    mail.send(msg)
