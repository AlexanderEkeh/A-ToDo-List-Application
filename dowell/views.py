from dowell import app
from flask import render_template, flash, redirect, request, url_for
from wtforms import Form, BooleanField, TextField, PasswordField, validators


notifi_count = 0
req_count = 0
my_path = []

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25, message=None)])
    email = TextField('Email', [validators.Email(message = "Please enter a valid email address.")])
    password = PasswordField('Password', [validators.Required(), validators.Length(min=8, max=-1, message=None)])
    confirm = PasswordField('Confirm Password',[validators.EqualTo('password', message='Must match password.')])

class LoginForm(Form):
    email = TextField('Email Address', [validators.Required(), validators.Email(message = 'Please enter a valid email address.') ])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('Remember me?')

@app.route('/')
@app.route('/index')
def index():
	login_link = True
	return render_template('index.html', login_link = login_link)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = RegistrationForm(request.form)
    if request.method == 'POST' and signup_form.validate():
        #user = User(form.username.data, form.email.data, form.password.data)
        #db_session.add(user)
        return redirect(url_for('welcome'))
    return render_template('signup.html', signup_form = signup_form, login_link = "no_display", page_title = "Sign Up")

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        return redirect(url_for('personal'))
    return render_template('login.html', login_form = login_form, login_link = "no_display", page_title = "Log In")

@app.route('/welcome')
def welcome():
	login_link = "welcome"
	page_title = "Welcome"
	return render_template('welcome.html', login_link = login_link, page_title = page_title)

@app.route('/personal')
def personal():
    page_title = "Personal"
    page_heading = "Add Personal Tasks"
    return render_template('addtask.html', req_count = req_count, notifi_count = notifi_count,
                login_link = False, page_title = page_title, page_heading = page_heading)

@app.route('/<path:path>')
def catch_all(path):
	my_path = path.split('/')
	login_link = False
	page_title = my_path[len(my_path) - 1]
	page_link = ""
	page_heading = ""
	if page_title == 'today':
		page_title = "Today"
		page_heading = "Events Scheduled for Today"
		page_link = "today.html"
	elif page_title == 'next':
		page_title = "This Week"
		page_heading = "Events for Next Seven(7) Days"
		page_link = "today.html"
	elif page_title == 'work':
		page_title = "Work"
		page_heading = "Add Work Related Tasks"
		page_link = "addtask.html"
	elif page_title == 'ceremony':
		page_title = "Ceremony"
		page_heading = "Add Ceremonies to Attend"
		page_link = "addtask.html"
	elif page_title == 'shopping':
		page_title = "Shopping"
		page_heading = "Add Shoppings to do"
		page_link = "addtask.html"
	elif page_title == 'general':
		page_title = "General"
		page_heading = "Add General Task"
		page_link = "addtask.html"
	elif page_title == 'travel':
		page_title = "Travel"
		page_heading = "Add Places to Visit"
		page_link = "addtask.html"		
	return render_template(page_link, req_count = req_count, notifi_count = notifi_count,
		 login_link = login_link, page_title = page_title, page_heading = page_heading)
