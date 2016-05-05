from dowell import app, db, lm
from flask import render_template, flash, redirect, request, url_for, session, g
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask.ext.login import login_user, logout_user, current_user, login_required
from .models import User

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

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', req_count = req_count, notifi_count = notifi_count, layout = "full")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_form = RegistrationForm(request.form)
    if request.method == 'POST' and signup_form.validate():
        u_name = signup_form.username.data
        u_mail = signup_form.email.data
        u_pass = signup_form.password.data
        u_data = User.query.all()
        for user in u_data:
            if u_mail == user.email or u_name == user.username:
                flash('Username or Email already exists. Select another to proceed or login.')
                return redirect(url_for('signup'))
        new_user = User(username = u_name, email = u_mail, password = u_pass)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('welcome'))
    return render_template('signup.html', signup_form = signup_form, page_title = "Sign Up", layout = "center")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        session['remember_me'] = login_form.remember_me.data
        u_mail = login_form.email.data
        p_word = login_form.password.data
        u_data = User.query.all()
        for user in u_data:
            if u_mail == user.email and p_word == user.password:
                if 'remember_me' in session:
                    remember_me = session['remember_me']
                    session.pop('remember_me', None)
                login_user(user, remember = remember_me)
                return redirect(request.args.get('next') or url_for('personal'))
        remember_me = False
        flash('Invalid Login. Please try again.')
        return redirect(url_for('login'))
    return render_template('login.html', login_form = login_form, page_title = "Log In", layout = "center")

@app.route('/welcome')
def welcome():
	login_link = "welcome"
	page_title = "Welcome"
	return render_template('welcome.html', login_link = login_link, page_title = page_title,
                          req_count = req_count, notifi_count = notifi_count, layout = "full")

@app.route('/personal')
@login_required
def personal():
    page_title = "Personal"
    page_heading = "Add Personal Tasks"
    return render_template('addtask.html', req_count = req_count, notifi_count = notifi_count,
                           page_title = page_title, page_heading = page_heading)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/<path:path>')
@login_required
def catch_all(path):
	my_path = path.split('/')
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
		 page_title = page_title, page_heading = page_heading, layout = "center")
