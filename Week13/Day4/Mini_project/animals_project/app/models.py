import datetime
from app import db


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    gender = db.Column(db.String(1))
    breed = db.Column(db.String(64))
    date_of_birth = db.Column(db.Date, nullable=True, default=datetime.date.today())
    details = db.Column(db.Text)
    price = db.Column(db.Integer)
    image = db.Column(db.String(100))
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pets = db.relationship('Pet', backref='cart', lazy='dynamic')

    def add_to_cart(self, pet_id):
        pet = Pet.query.get(pet_id)
        new_pet = pet
        if pet:
            self.pets.append(new_pet)
            db.session.add(self)
            db.session.commit()

    # def remove(self, pet_id):
    #     pet = Pet.query.get(pet_id)
    #     if pet:
    #         self.pets.remove(pet)
    #         db.session.commit()

    def get_cart(self):
        return [cart.id for cart in self.query.all()]

    def total(self):
        total = 0
        pets = Pet.query.all()
        pets_prices = [pet.price for pet in pets if pet.cart_id in self.get_cart()]
        for price in pets_prices:
            total += price
        return total


