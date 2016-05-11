from wtforms import Form, BooleanField, TextField, PasswordField, validators, TextAreaField

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25, message=None)])
    email = TextField('Email', [validators.Email(message = "Please enter a valid email address.")])
    password = PasswordField('Password', [validators.Required(), validators.Length(min=8, max=-1, message=None)])
    confirm = PasswordField('Confirm Password',[validators.EqualTo('password', message='Must match password.')])

class LoginForm(Form):
    email = TextField('Email Address', [validators.Required(), validators.Email(message = 'Please enter a valid email address.') ])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('Remember me?')
	
class TaskForm(Form):
    task_head = TextField('Title', [validators.Required()])
    task_desc = TextAreaField('Description', [validators.Required()])
    task_date = TextField('Date', [validators.Required()])
    task_time = TextField('Time',[validators.Required()])