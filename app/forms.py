from flask.ext.wtf import Form
from wtforms import StringField, IntegerField
from flask_wtf.html5 import EmailField
from wtforms.validators import DataRequired

class UserForm(Form):
    nickname = StringField('nickname', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])


class TripForm(Form):
    destination = StringField('destination', validators=[DataRequired()])
    name_of_trip = StringField('name_of_trip', validators=[DataRequired()])
    trip_date = StringField('trip_date', validators=[DataRequired()])
    duration = StringField('duration', validators=[DataRequired()])
    budget = StringField('budget', validators=[DataRequired()])
    add_friend = StringField('add_friend', validators=[DataRequired()])