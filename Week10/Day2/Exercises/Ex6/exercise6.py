# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message
# stating how many minutes the user lived in his life.
import datetime

def life_in_minutes(birthday):
    birthday_date = datetime.datetime.strptime(birthday, '%Y/%m/%d')
    today = datetime.datetime.today()
    life = today - birthday_date
    print(f"You live {int(life.days * 24 * 60 + life.seconds / 60)} minutes")

life_in_minutes(input('Enter your birthday date (format: year/month/day): '))