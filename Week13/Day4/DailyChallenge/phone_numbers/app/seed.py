from app import db, models
from faker import Faker

fake = Faker()

for _ in range(30):
    fake_name = fake.name()
    fake_address = fake.address()
    fake_email = ''.join(fake_name.lower().split(' ')) + '@gmail.com'
    fake_number = fake.phone_number()
    person_table = models.Person(name=fake_name, address=fake_address, email=fake_email)
    db.session.add(person_table)
    db.session.commit()
    phnumber_table = models.Phonenumber(number=fake_number, owner=person_table.person_id)
    db.session.add(phnumber_table)
    db.session.commit()
