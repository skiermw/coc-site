from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, SelectField, StringField
from wtforms.validators import DataRequired, InputRequired, Required

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class Attendee(FlaskForm):
	fullname = StringField('Full Name')
	fname = StringField('First Name', validators=[InputRequired()])
	mname = StringField('Middle Name')
	lname = StringField('Last Name', validators=[InputRequired()])
	type =  SelectField(u'Type', choices=[('Agent', 'Agent'),
										  ('DSM/RSM','DSM/RSM'),
										  ('Officer','Offficer'),
										  ('Board Member', 'Board Member'),
										  ('Guest', 'Guest'),
										  ('Staff', 'Staff')], validators = [DataRequired()])
	
class Attendee_Schedule(FlaskForm):
	fname = StringField('First Name', validators=[InputRequired()])
	mname = StringField('Middle Name')
	lname = StringField('Last Name', validators=[InputRequired()])
