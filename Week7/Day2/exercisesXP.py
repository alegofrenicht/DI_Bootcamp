from random import randint

# Exercise 1 : What Are You Learning ?
# Instructions
# 1. Write a function called display_message() that prints one sentence telling everyone what you are learning
#    in this course.
# 2. Call the function, and make sure the message
# displays correctly.

# def display_message():
#     print('Python and JS')
#
# display_message()


# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# 1. Write a function called favorite_book() that accepts one parameter called title.
# 2. The function should print a message, such as "One of my favorite books is <title>".
#    For example: “One of my favorite books is Alice in Wonderland”
# 3. Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f'One of my favorite books is {title}')


favorite_book('American Psyco')


# 🌟 Exercise 3 : Some Geography
# Instructions
# 1. Write a function called describe_city() that accepts the name of a city and its country as parameters.
# 2. The function should print a simple sentence, such as "<city> is in <country>".
#    For example “Reykjavik is in Iceland”
# 3. Give the country parameter a default value.
# 4. Call your function.

def describe_city(city, country='Israel'):
    print(f'{city} is in {country}')


describe_city('Tel Aviv')

# Exercise 4 : Random
# Instructions
# 1. Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# 2. Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and
#    display both numbers.


def randomiser(number):
    second_number = randint(1, 100)
    if number == second_number:
        print('Congratulations, it\'s a match')
    else:
        print(f'Sorry, number was {second_number} and your try was {number}')


randomiser(int(input('choose your number:\n')))


# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# 1. Write a function called make_shirt() that accepts a size and the text of a message that should be printed
#    on the shirt.
# 2. The function should print a sentence summarizing the size of the shirt and the message printed on it,
#    such as "The size of the shirt is <size> and the text is <text>"
# 3. Call the function make_shirt().
# 4. Modify the make_shirt() function so that shirts are large by default with a message that reads
#    “I love Python” by default.
# 5. Make a large shirt with the default message
# 6. Make medium shirt with the default message
# 7. Make a shirt of any size with a different message.
# 8. Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size='large', text='I love Python'):
    print(f'The size of the shirt is {size} and the text is "{text}"')


make_shirt()
make_shirt('medium')
make_shirt(text='Hello')
make_shirt(size='XXL', text='I\'m bigboi')

# 🌟 Exercise 6 : Magicians …
# Instructions
# 1. Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# 2. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# 3. Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great"
#    to each magician’s name.
# 4. Call the function make_great().
# 5. Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def make_great(any_list):
    for index in range(len(any_list)):
        any_list[index] += ' the Great'


def show_magicians(magicians):
    make_great(magician_names)
    for magician in magicians:
        print(magician)


show_magicians(magician_names)
