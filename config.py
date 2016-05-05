import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-need-to-know-me-to-know-it'

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dowell.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')