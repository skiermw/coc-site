from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, SelectField, StringField, DateField, FormField
from wtforms.validators import DataRequired, InputRequired, Email

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class AttendeeType(FlaskForm):
	type = SelectField(u'Type', choices=[('Agent', 'Agent'),
										 ('DSM', 'DSM'),
										 ('RSM', 'RSM'),
										 ('Officer', 'Offficer'),
										 ('Board Member', 'Board Member'),
										 ('Guest', 'Guest'),
										 ('Staff', 'Staff')], validators=[DataRequired()])


class Attendee(FlaskForm):
	firstName = StringField('First Name', validators=[InputRequired()])
	middleName = StringField('Middle Name')
	lastName = StringField('Last Name', validators=[InputRequired()])
	preferredName = StringField('Preferred Name', validators=[InputRequired()])
	birthdDate = DateField('Date of Birth', validators=[InputRequired()], format='%m/%d/%Y')
	cellPhone = StringField('Cell Phone Number', validators=[InputRequired()])
	email = StringField('Email', validators=[Email(), InputRequired()])

class Location(FlaskForm):
	city = StringField('City', validators=[InputRequired()])
	state = StringField('State', validators=[InputRequired()])

class Agent(FlaskForm):
	attendee = FormField(Attendee)
	agentNumber = StringField('Agent Number', validators=[InputRequired()])
	stateNumber = StringField('Agency State Number', validators=[InputRequired()])
	districtNumber = StringField('Agency District Number', validators=[InputRequired()])
	location = FormField(Location)

class DSM(FlaskForm):
	attendee = FormField(Attendee)
	stateNumber = StringField('Agency State Number', validators=[InputRequired()])
	districtNumber = StringField('Agency District Number', validators=[InputRequired()])
	location = FormField(Location)

class Guest(FlaskForm):
	attendee = FormField(Attendee)

class Officer(FlaskForm):
	attendee = FormField(Attendee)
	title = StringField('Officer Title', validators=[InputRequired()])
	department = StringField('Officer Department', validators=[InputRequired()])
	location = FormField(Location)

class BoardMember(FlaskForm):
	attendee = FormField(Attendee)

class Staff(FlaskForm):
	attendee = FormField(Attendee)

class Attendee_Schedule(FlaskForm):
	fname = StringField('First Name', validators=[InputRequired()])
	mname = StringField('Middle Name')
	lname = StringField('Last Name', validators=[InputRequired()])
