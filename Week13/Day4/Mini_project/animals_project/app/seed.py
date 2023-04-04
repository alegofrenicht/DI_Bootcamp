from app import db, models, flask_app
import datetime


def seed():

    pets = [
        ['Dog', 'F',  'Poodle', '2010-03-15', 'Nice and fluffy dog', 1000, 'https://dogfriendlyscene.co.uk/wp-content/uploads/2020/09/poodle-with-a-show-clip.png'],
        ['Cat', 'M', 'British shorthair', '2019-08-01', 'Likes to eat and sleep', 500, 'https://www.purina.co.uk/sites/default/files/styles/square_medium_440x440/public/2022-06/British-Shorthair.jpg?itok=eFXNhiXz'],
        ['Parrot', 'M', 'Sun Conure', '2009-10-05', 'Medium-sized, vibrantly colored parrot native to northeastern South America', 600, 'https://zupreem.com/wp-content/uploads/2020/11/shutterstock_155146361-scaled.jpg']
        ]

    print('Started')

    models.Pet.query.delete()
    models.Cart.query.delete()
    db.session.commit()


    for pet in pets:
        pet_table = models.Pet(
            name=pet[0],
            gender=pet[1],
            breed=pet[2],
            date_of_birth=datetime.datetime.strptime(pet[3], '%Y-%m-%d').date(),
            details=pet[4],
            price=pet[5],
            image=pet[6],

        )
        db.session.add(pet_table)
        db.session.commit()
