from webapp import app, db
from flask import render_template, flash, redirect, url_for, session, request
from webapp.forms import LoginForm, RegisterForm
from webapp.models import AppUser, CryptoCurrency, user_crypto_currency
import api
from random import choice


@app.route('/')
@app.route('/currencies')
def currencies_page():
    currencies = api.api_func()
    return render_template('currencies.html', currencies=currencies)


@app.route('/home', methods=("GET", "POST"))
def home():
    form = LoginForm()
    login = AppUser.query.filter_by(email=form.mail.data).first()
    if form.validate_on_submit():
        if login:
            session['user_name'] = login.username
            session['logged_in'] = True
            flash(f'Good to see you, {login.username}!')
            return redirect(url_for('user_page', user=login.username))
        else:
            flash('Invalid username or password')
            return redirect(url_for('home'))

    return render_template('home.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    # remove the user ID from the session
    session.pop('user_name', None)
    session.pop('logged_in', None)
    flash('You were logged out', 'warning')
    return redirect(url_for('home'))


@app.route('/register', methods=("GET", "POST"))
def register():
    form = RegisterForm()
    user_from_db = AppUser.query.filter_by(email=form.mail.data).first()
    if form.validate_on_submit():
        if user_from_db:
            flash('User already exists')
            return redirect(url_for('register'))
        else:
            user = AppUser(username=form.username.data, email=form.mail.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/user/<user>')
def user_page(user):
    user_from_db = AppUser.query.filter_by(username=user).first()
    currencies = AppUser.query.filter_by(username=user).first().cryptocurrencies
    if user_from_db:
        return render_template('user_page.html', user=user_from_db, currencies=currencies)
    else:
        return redirect(url_for('home'))

@app.route('/add_currency/<user>/<currency_id>')
def add_currency(user, currency_id):
    if not session.get('logged_in'):
        flash('You need to login first')
        return redirect(url_for('home'))
    currency = [curr for curr in api.api_func() if curr['id'] == int(currency_id)][0]
    existing_currency = CryptoCurrency.query.filter_by(id=currency_id).first()
    if not existing_currency:
        currency_to_add = CryptoCurrency(id=currency['id'], name=currency['name'], symbol=currency['symbol'], slug=currency['slug'], first_historical_data=currency['first_historical_data'], last_historical_data=currency['last_historical_data'])
        db.session.add(currency_to_add)
        db.session.commit()
    else:
        user_from_db = AppUser.query.filter_by(username=user).first()
        currency = CryptoCurrency.query.filter_by(id=currency_id).first()
        if currency in user_from_db.cryptocurrencies:
            flash(f'Currency {currency.name} already in your list')
            return redirect(url_for('currencies_page'))
        user_from_db.cryptocurrencies.append(currency)
        db.session.commit()
        flash(f'Currency {currency.name} added to your list')
        return redirect(url_for('currencies_page'))
    flash('Currency not found')
    return redirect(url_for('home'))


@app.route('/remove_currency/<user>/<currency_id>')
def remove_currency(user, currency_id):
    if not session.get('logged_in'):
        flash('You need to login first')
        return redirect(url_for('home'))
    currency = CryptoCurrency.query.filter_by(id=currency_id).first()
    if currency:
        user_from_db = AppUser.query.filter_by(username=user).first()
        user_from_db.cryptocurrencies.remove(currency)
        db.session.commit()
        flash(f'Currency {currency.name} removed from your list')
        return redirect(url_for('user_page', user=user))

