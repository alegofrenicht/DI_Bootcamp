from app import flask_app, models, db, seed
from flask import render_template, url_for, redirect


@flask_app.route('/seed_data')
def seed_data():
    seed.seed()
    return redirect(url_for('pets'))


@flask_app.route('/')
def index():
    return render_template('index.html')

@flask_app.route('/pets')
def pets():
    data = models.Pet.query.all()
    return render_template('pets.html', data=data)


@flask_app.route('/pets/<int:id>')
def pet_page(id):
    data = models.Pet.query.filter_by(id=id).first()
    return render_template('pet.html', pet=data)


@flask_app.route('/add_pet/<int:id>')
def add_pet(id):
    models.Cart().add_to_cart(id)
    return redirect(url_for('pets'))

@flask_app.route('/cart')
def cart_page():
    data = models.Cart().get_cart()
    all_pets = models.Pet.query.all()
    total = models.Cart().total()
    return render_template('cart.html', cart=data, pets=all_pets, total=total)

# @flask_app.route('/remove/<int:id>')
# def remove_page(id):
#     models.Cart().remove(id)
#     return redirect(url_for('cart_page'))

