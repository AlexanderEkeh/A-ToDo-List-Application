from dowell import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(32), index = True, unique = True)
	email = db.Column(db.String(120), index = True, unique = True)
	password = db.Column(db.String(120), index = True)
	tasks = db.relationship('Tasks', backref='owner', lazy='dynamic')
	comments = db.relationship('Comments', backref='owner', lazy='dynamic')
	votes = db.relationship('Votes', backref='owner', lazy='dynamic')
	
	@property
	def is_authenticated(self):
		return True
	
	@property
	def is_active(self):
		return True
    
	@property
	def is_anonymous(self):
		return False
	
	def get_id(self):
		try:
			return unicode(self.id) #python 2
		except NameError:
			return str(self.id) #python 3
		
	def __repr__(self):
		return '<User %r' % (self.username)

class Tasks(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	category = db.Column(db.String(50))
	title = db.Column(db.String(200))
	description = db.Column(db.String(600))
	due_date = db.Column(db.String(13))
	due_time = db.Column(db.String(8))
	reminder_date = db.Column(db.String(13))
	reminder_time = db.Column(db.String(8))
	requests = db.Column(db.String(10))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	comments = db.relationship('Comments', backref='task', lazy='dynamic')
	
	def __repr(self):
		return '<Tasks %r' % (self.title)

class Comments(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	comment = db.Column(db.String(300))
	task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	votes = db.relationship('Votes', backref='comment', lazy='dynamic')
	
	def __repr__(self):
		return 'Comment %r' % (self.comment)
	
class Votes(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	vote = db.Column(db.String(10))
	comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	def __repr__(self):
		return 'Vote %r' % (self.vote)