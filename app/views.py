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
    

        # return redirect('/users')
    return render_template('login.html', form=form)

@myapp.route('/index')
def index():
    nickname = ''
    if 'nickname' in session:
        username = escape(session['nickname'])
        return render_template('survey.html', name=nickname)
    else:
        return render_template('login.html')


@myapp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        session['nickname'] = request.form.get("nickname")
        session['email'] = request.form.get("email")
        return redirect(url_for('index'))


@app.route('/users')
def display_user():
    # Retreive data from database to display
    customers = retrieve_customers(None)
    orders = retrieve_orders(None)
    addresses = retrieve_addresses(None)
    return render_template('home.html',
                            customers=customers, orders=orders, addresses=addresses)

@app.route('/create_trip/<customer_id>', methods=['GET', 'POST'])
def create_trip(customer_id):
    form = TripForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        insert_order(name_of_part, manufacturer_of_part, customer_id)
        return redirect('/customers')
    return render_template('order.html', form=form)

@app.route('/create_trip/<customer_id>', methods=['GET', 'POST'])
def delete_trip(customer_id):
        form = TripForm()
    if form.validate_on_submit():
        # Get data from the form
        # Send data from form to Database
        name_of_part = form.name_of_part.data
        manufacturer_of_part = form.manufacturer_of_part.data
        insert_order(name_of_part, manufacturer_of_part, customer_id)
        return redirect('/customers')
    return render_template('order.html', form=form)


