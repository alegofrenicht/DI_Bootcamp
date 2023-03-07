# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.

from random import randint

user_num = int(input('enter num between 1 and 100: '))


def guess(num):
    return 'Success' if num == randint(1, 100) else None

print(guess(user_num))