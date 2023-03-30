from flask import render_template, flash, redirect, url_for
from app import flask_app
from app import models
from app.forms import LoginForm
from app import db
import json



@flask_app.route('/')
def populate():
    with open('app/static/users.json', 'r') as file_obj:
        robots = json.load(file_obj)
    models.User.query.delete()
    for user in robots:
        model = models.User(name=user['name'], street=user['address']['street'], city=user['address']['city'], zipcode=user['address']['zipcode'])
        db.session.add(model)
    db.session.commit()
    data_1 = models.User.query.all()
    data_2 = models.User.query.filter_by(city='Roscoeview').all()
    data_3 = models.User.query.limit(5)
    data_4 = models.User.query.filter(models.User.zipcode.startswith('5')).all()
    return render_template('index.html', data_1=data_1, data_2=data_2, data_3=data_3, data_4=data_4)


@flask_app.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_name = form.name.data
        if ',' in form.address_city.data:
            street, city = form.address_city.data.split(',')
            data = models.User.query.filter_by(name=login_name.strip(), city=city.strip(), street=street.strip()).first()
            if data:
                flash("You're logged in")
                return render_template('main.html', data=data)
            else:
                if form.address_city.data.isdigit() or login_name.isdigit():
                    flash('Error! Incorrect credentials', 'error')
                    return redirect(url_for('login'))
                flash('Sign up')
                return redirect(url_for('login'))



    return render_template('login.html', form=form)
