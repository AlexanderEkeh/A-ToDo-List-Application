import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-need-to-know-me-to-know-it'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dowell.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['aezumezu@gmail.com']