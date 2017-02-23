from app import app
from flask import Flask, render_template, request, redirect, session, flash, url_for
from .forms import LoginForm, Agent
import urllib2
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    flash('Flash!!', 'alert')
    if 'username' in session:
        user = session['username']
        return render_template('index.html', user = user)
    else:
        return redirect('/login')

@app.route('/add_agent', methods=['GET', 'POST'])
def add_agent():
    form = Agent()
    if form.validate_on_submit():
        flash('Agent added', 'success')
        print(form.data)
        return redirect(url_for('add_agent'))
    return render_template('agent.html',
                           title='Add Agent',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    #session['username'] = "Mark Workman"
    if form.validate_on_submit():
        '''
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        '''
        session['username'] = request.form['username']
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/attendee_schedule')
def attendee_schedule():
    user = session['username']
    user = 'MarkWorkman'
    url = 'https://3ldsu710o2.execute-api.us-east-1.amazonaws.com/dev/coc/api/v1.0/schedule/%s' % user
    #url = 'https://3ldsu710o2.execute-api.us-east-1.amazonaws.com/dev/coc/api/v1.0/schedule/MarkWorkman'
    response = urllib2.urlopen(url).read()
    #response = requests.put(url)
    print(response)
    events_json = json.loads(response)
    return render_template('schedule.html', user=user, events=events_json)

@app.route('/attendees')
def attendees():
    url = 'https://3ldsu710o2.execute-api.us-east-1.amazonaws.com/dev/coc/api/v1.0/attendees'
    response = urllib2.urlopen(url).read()
    attendees_json = json.loads(response)
    return render_template('attendees.html', attendees=attendees_json)

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))