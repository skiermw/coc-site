from app import app
from flask import Flask, render_template, flash, redirect, session
from .forms import LoginForm, Attendee
import urllib2
import json

@app.route('/')
@app.route('/index')
def index():
    if 'user' in session:
        return render_template('index.html')
    else:
        return redirect('/login')
        '''
        form = LoginForm()
        return render_template('login.html',
                           title='Sign In',
                           form=form)
        '''

@app.route('/attendee', methods=['GET', 'POST'])
def attendee():
    form = Attendee()
    return render_template('attendee.html',
                           title='Attendee',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        '''
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        '''
        session['user'] = "MarkWorkman"
        return redirect('/index')
    return render_template('login.html',
                           title='Sign In',
                           form=form)

@app.route('/attendee_schedule')
def attendee_schedule():
    user = session['user']
    url = 'https://3ldsu710o2.execute-api.us-east-1.amazonaws.com/dev/coc/api/v1.0/schedule/%s' % user
    response = urllib2.urlopen(url).read()
    print(response)
    events_json = json.loads(response)
    return render_template('attendee_schedule.html', user=user, events=events_json)

@app.route('/attendees')
def attendees():
    url = 'https://3ldsu710o2.execute-api.us-east-1.amazonaws.com/dev/coc/api/v1.0/attendees'
    response = urllib2.urlopen(url).read()
    attendees_json = json.loads(response)
    return render_template('attendees.html', attendees=attendees_json)