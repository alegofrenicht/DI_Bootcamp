from app import flask_app, models
from flask import render_template, flash, redirect, url_for


@flask_app.route('/person/<string>')
def fromstring(string):
    number = models.Phonenumber.query.filter_by(number=string).first()
    if number:
        person = models.Person.query.filter_by(person_id=number.owner).first()
        return render_template('from_number.html', number=number, person=person)
    else:
        person = models.Person.query.filter_by(name=string).first()
        if person:
            number = models.Phonenumber.query.filter_by(owner=person.person_id).first()
            return render_template('from_person.html', number=number, person=person)
        else:
            flash('No results found', 'error')
            return render_template('error.html')
