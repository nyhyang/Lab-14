from flask import render_template, redirect, request
from app import app, models, db
from .forms import UserForm, TripForm
from .models import *
# Access the models file to use SQL functions


@app.route('/')
def index():
    return redirect('/create_user')

@app.route('/create_user', methods=['GET', 'POST'])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        nickname = form.nickname.data
        email = form.email.data
        insert_user(nickname, email)

        # return redirect('/users')
    return render_template('login.html', form=form)

# @myapp.route('/index')
# def index():
#     nickname = ''
#     if 'nickname' in session:
#         username = escape(session['nickname'])
#         return render_template('survey.html', name=nickname)
#     else:
#         return render_template('login.html')


@myapp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session['nickname'] = request.form.get("nickname")
        session['email'] = request.form.get("email")
        return redirect(url_for('index'))


@app.route('/users')
def display_trip():
    # Retreive data from database to display
    trips = retrieve_trip(None)    
    return render_template('tripfeed.html',
                            trips=trips)

@app.route('/create_trip/<user_id>', methods=['GET', 'POST'])
def create_trip(user_id):
    form = TripForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        destination = form.destination.data
        name_of_trip = form.name_of_trip.data
        trip_date = form.trip_date.data
        duration = form.duration.data
        budget = form.budget.data
        friend = form.friend.data
        create_trip(destination, name_of_trip, trip_date, duration, budget, friend, user_id)
        return redirect('/customers')
    return render_template('order.html', form=form)

@app.route('/delete_trip/<trip_id>', methods=['GET', 'POST'])
def delete_trip(trip_id):
    delete_trip(trip_id)
    return render_template('tripfeed.html', form=form)


