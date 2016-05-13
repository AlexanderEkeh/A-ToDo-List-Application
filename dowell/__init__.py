import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from config import basedir
from flask.ext.mail import Mail

app = Flask(__name__)
app.config.from_object('config')
app.config['OAUTH_CREDENTIALS'] = {
    'facebook': {
        'id': '1771436973087378',
        'secret': '71bdb49d9fb9b6f856dcf51e63523ace'
    },
    'twitter': {
        'id': ' thR3b6CKN9sBT9aA2OifIGtjj',
        'secret': 'sXsiLQHZCWtkGbRXkm3C9glbnHlFZahzdJ3JR4RkXghhWRb5DM'
    }
}
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

mail = Mail(app)

from dowell import views, models
