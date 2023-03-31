from app import db


class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    address = db.Column(db.String(64))
    phonenumbers = db.relationship('Phonenumber', backref='person', lazy='dynamic')

class Phonenumber(db.Model):
    number_id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(32))
    owner = db.Column(db.Integer, db.ForeignKey('person.person_id'))




