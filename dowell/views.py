from dowell import app, db, lm
from flask import render_template, flash, redirect, request, url_for, session, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from .models import User, Tasks
from .forms import RegistrationForm, LoginForm, TaskForm
from sqlalchemy import and_
import datetime
from .emails import task_reminder

notifi_count = 0
req_count = 0
my_path = []


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.before_request
def before_request():
    g.user = current_user

def get_rem_detail(taskid):
	rem_data = []
	task = Tasks.query.filter(Tasks.id == taskid).all()
	user = User.query.filter(User.id == task[0].user_id).all()
	rem_data.append(user[0].username)
	rem_data.append(task[0].title)
	rem_data.append(task[0].due_date)
	rem_data.append(task[0].due_time)
	return rem_data

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
		login_user(new_user)
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
                return redirect(request.args.get('next') or url_for('add_task'))
        remember_me = False
        flash('Invalid Login. Please try again.')
        return redirect(url_for('login'))
    return render_template('login.html', login_form = login_form, page_title = "Log In", layout = "center")

@app.route('/welcome')
def welcome():
	login_link = "welcome"
	page_title = "Welcome"
	task_reminder([g.user.username], 'signup', g.user.email)
	return render_template('welcome.html', login_link = login_link, page_title = page_title,
                          req_count = req_count, notifi_count = notifi_count, layout = "full")

def get_rem_time(my_time):
	am_or_pm = ""
	st = len(my_time) - 2
	hour = my_time.split(":")
	mins = hour[1]
	mins = mins[:2]
	day = '0'
	hour = hour[0]
	if my_time[st:] == 'am' and int(hour) - 1 == 11:
		hour = 11
		am_or_pm = 'pm'
		day = '-1'
	elif my_time[st:] == 'am':
		hour = int(hour) - 1
		am_or_pm = 'am'
	elif my_time[st:] == 'pm' and int(hour) - 1 == 11:
		hour = 11
		am_or_pm = 'am'
	elif my_time[st:] == 'pm':
		hour = int(hour) - 1
		am_or_pm = 'pm'
	if hour == 0:
		hour = 12
	time = str(hour) + ':' + str(mins) + am_or_pm
	return [time, day]

def addtask(my_form):
	rem_date = ""
	referrer = request.headers.get("Referer")
	referrer_path = referrer.split('/')
	referrer = referrer_path[len(referrer_path) - 1]
	if request.method == 'POST' and my_form.validate():
		task_head = my_form.task_head.data
		task_desc = my_form.task_desc.data
		task_date = my_form.task_date.data
		task_time = my_form.task_time.data
		task_rem_time = get_rem_time(task_time)[0]
		task_rem_date = task_date
		if get_rem_time(task_time)[1] == '-1':
			rem_date = task_date.split("/")
			rem_date = int(rem_date[1]) - 1
			if len(rem_date) == 1:
				rem_date = '0' + str(rem_date)
			task_rem_date = rem_date
		task_data = Tasks(category = referrer, title = task_head, description = task_desc, due_date = task_date, due_time = task_time, user_id = g.user.get_id(), reminder_date = task_rem_date, reminder_time = task_rem_time)
		db.session.add(task_data)
		db.session.commit()
	return referrer

def get_tasks(group):
	return Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.category == group)).all()

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/today', methods=['GET', 'POST'])
@login_required
def day_event():
	page_title = "Today"
	page_heading = "Events Scheduled for Today"
	day = datetime.datetime.now()
	day_date = day.strftime('%m/%d/%Y')
	Tasks.query.order_by(Tasks.due_time)
	task_today = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == day_date)).all()
	return render_template("today.html", req_count = req_count, notifi_count = notifi_count, page_title = page_title, page_heading = page_heading, layout = "center", task_today = task_today)

def get_day(num):
	d_day = (datetime.date.today() + datetime.timedelta(days=num))
	d_day = d_day.strftime('%m/%d/%Y')
	return d_day

def get_day_of_week(num):
	day_dict = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
	d_day = (datetime.date.today() + datetime.timedelta(days=num))
	d_day = day_dict[d_day.weekday()] + ", " + d_day.strftime('%m - %d - %Y')
	return d_day

@app.route('/next', methods=['GET', 'POST'])
@login_required
def week_event():
	days = []
	page_title = "This Week"
	page_heading = "Events for Next Seven(7) Days"
	task_day1 = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == get_day(1))).all()
	task_day2 = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == get_day(2))).all()
	task_day3 = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == get_day(3))).all()
	task_day4 = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == get_day(4))).all()
	task_day5 = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == get_day(5))).all()
	task_day6 = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == get_day(6))).all()
	task_day7 = Tasks.query.filter(and_(Tasks.user_id == g.user.get_id(), Tasks.due_date == get_day(7))).all()
	for i in range(1, 8):
		days.append(get_day_of_week(i))
	return render_template("thisweek.html", req_count = req_count, notifi_count = notifi_count, page_title = page_title, page_heading = page_heading, layout = "center", task_day1 = task_day1, task_day2 = task_day2, task_day3 = task_day3, task_day4 = task_day4, task_day5 = task_day5, task_day6 = task_day6, task_day7 = task_day7, days = days)

@app.route('/addtask', methods=['POST'])
@app.route('/personal', methods=['GET', 'POST'])
@app.route('/work', methods=['GET', 'POST'])
@app.route('/ceremony', methods=['GET', 'POST'])
@app.route('/shopping', methods=['GET', 'POST'])
@app.route('/general', methods=['GET', 'POST'])
@app.route('/travel', methods=['GET', 'POST'])
@login_required
def add_task():
	link = request.path
	link_path = link.split('/')
	link = link_path[len(link_path) - 1]
	task_form = TaskForm(request.form)
	if link == 'personal' or link == 'login' or link == 'signup':
		page_heading = "Add Personal Tasks"
	elif link == 'work':
		page_heading = "Add Work Related Tasks"
	elif link == 'ceremony':
		page_heading = "Add Ceremonies to Attend"
	elif link == 'shopping':
		page_heading = "Add Shoppings to do"
	elif link == 'general':
		page_heading = "Add General Task"
	elif link == 'travel':
		page_heading = "Add Places to Visit"
	elif link == 'addtask':
		return redirect(addtask(task_form))
	task_data = get_tasks(link)
	return render_template("addtask.html", req_count = req_count, notifi_count = notifi_count, page_title = link.capitalize(), page_heading = page_heading, layout = "center",  task_form = task_form, task_data = task_data)


@app.route('/req_personal', methods=['GET', 'POST'])
@app.route('/req_work', methods=['GET', 'POST'])
@app.route('/req_ceremony', methods=['GET', 'POST'])
@app.route('/req_shop', methods=['GET', 'POST'])
@app.route('/req_general', methods=['GET', 'POST'])
@app.route('/req_notify', methods=['GET', 'POST'])
@app.route('/req_travel', methods=['GET', 'POST'])
@login_required
def comment():
	link = request.path
	link_path = link.split('/')
	link = link_path[len(link_path) - 1]
	if link == 'req_personal':
		page_title = "Personal Requests"
	elif link == 'req_work':
		page_title = "Work Requests"
	elif link == 'req_ceremony':
		page_title = "Ceremony Requests"
	elif link == 'req_shop':
		page_title = "Shopping Requests"
	elif link == 'req_general':
		page_title = "General Requests"
	elif link == 'req_notify':
		page_title = "Notifications Comments"
	elif link == 'req_travel':
		page_title = "Travel Request"
	return render_template("solutions.html", req_count = req_count, notifi_count = notifi_count, page_title = page_title, page_heading = page_title, layout = "center")
