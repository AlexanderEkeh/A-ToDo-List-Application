from dowell import app
from flask import render_template, flash, redirect, request, url_for

notifi_count = 0
req_count = 0
my_path = []

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
	login_link = True
	if request.method == 'POST':
		return redirect(url_for('today'))
	return render_template('index.html', login_link = login_link)


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
	elif page_title == 'personal':
		page_title = "Personal"
		page_heading = "Add Personal Tasks"
		page_link = "addtask.html"
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

