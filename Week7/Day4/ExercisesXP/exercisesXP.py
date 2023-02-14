from random import randint


# 🌟 Exercise 1 : Temperature Advice

def get_random_temp(season):
    if season == 'winter':
        return randint(-10, 10)
    elif season == 'fall' or season == 'autumn':
        return randint(10, 15)
    elif season == 'spring':
        return randint(15, 22)
    elif season == 'summer':
        return randint(22, 35)


def main():
    season = input('Choose the season:\n')
    temp = get_random_temp(season)
    print(f'The temperature right now is {temp} degrees Celcius.')
    if temp < 0:
        return "Brrr, that’s freezing! Wear some extra layers today"
    elif 0 <= temp <= 16:
        return "Quite chilly! Don’t forget your coat"
    elif 16 < temp <= 23:
        return "Weather is almost perfect, but be careful, it's still windy "
    elif 24 <= temp <= 32:
        return "Summertime sadness! Put suncream on your skin."


print(main())


# Exercise 2 : When Will I Retire ?


def get_age(year, month, day):
    year_today = [2023, 2, 14]

    if year_today[1] < month:
        return year_today[0] - year - 1
    elif year_today[1] == month and year_today[2] < day:
        return year_today[0] - year - 1
    else:
        return year_today[0] - year


def can_retire(gender, date_of_birth):
    age = get_age(*map(int, date_of_birth.split('/')))
    if gender == 'male':
        if age >= 67:
            return 'You can retire'
        else:
            return 'Back to work!'
    elif gender == 'female':
        if age >= 62:
            return 'You can retire'
        else:
            return 'Back to work!'
    else:
        return 'Sorry, choose from "male"/"female"'


gender_question = input('Please enter your gender (male/female):\n')
birth_question = input('PLease enter your birth date in next way - "year/month/day":\n')

print(can_retire(gender_question, birth_question))


# Exercise 3:
# Instructions
# Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
# Example:
#
# If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
#
# Hint: treating our number as a int or a str at different points in our code may be helpful

def multiple_addition(number):
    numbers = []
    for index in range(1, 5):
        numbers.append(str(number) * index)
    return sum(map(int, numbers))


print(multiple_addition(int(input('enter any number:'))))
