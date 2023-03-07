# Exercise 9 : Faker Module
# Instructions
# 1. Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# 2. Create an empty list called users. Tip: It should be a list of dictionaries.
# 3. Create a function that adds new dictionaries to the users list.
# Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

import faker as f

users = []
def userdata_merge():
    input('enter your name: ')
    input('enter your address: ')
    input('enter your language code : ')
    users.append({'name': f.Faker().name()})
    users.append({'address': f.Faker().address()})
    users.append({'language code': f.Faker().language_code()})


userdata_merge()
print(users)
