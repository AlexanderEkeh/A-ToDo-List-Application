from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
comments = Table('comments', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('comment', String(length=300)),
    Column('task_id', Integer),
    Column('user_id', Integer),
)

tasks = Table('tasks', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('category', String(length=50)),
    Column('title', String(length=200)),
    Column('description', String(length=600)),
    Column('due_date', String(length=13)),
    Column('due_time', String(length=8)),
    Column('reminder_date', String(length=13)),
    Column('reminder_time', String(length=8)),
    Column('requests', String(length=10)),
    Column('user_id', Integer),
)

votes = Table('votes', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('vote', String(length=10)),
    Column('comment_id', Integer),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comments'].create()
    post_meta.tables['tasks'].create()
    post_meta.tables['votes'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['comments'].drop()
    post_meta.tables['tasks'].drop()
    post_meta.tables['votes'].drop()
