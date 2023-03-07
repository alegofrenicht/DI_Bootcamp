# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the next upcoming
# holiday and print which holiday that is. (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

import datetime

def today():
    date_today = datetime.datetime.today()
    holidays = {'2023/5/1': 'Some other day'}
    next_holiday = []
    flag = False
    for year in range(2023, 2024 + 1):
        for month in range(1, 12 + 1):
            if flag:
                break
            for day in range(1, 31 + 1):
                date = f"{year}/{month}/{day}"
                if date in holidays:
                    next_holiday = [date, holidays[date]]
                    flag = True
                    break

    holiday = datetime.datetime.strptime(next_holiday[0], '%Y/%m/%d') - date_today
    if holiday.days < 1:
        print(f"{next_holiday[1]} is in {int(holiday.seconds / 3600)} hours")
    else:
        if holiday.days == 1:
            print(f"{next_holiday[1]} is in {holiday.days} day and {int(holiday.seconds / 3600)} hours")
        else:
            print(f"{next_holiday[1]} is in {holiday.days} days and {int(holiday.seconds / 3600)} hours")

today()
