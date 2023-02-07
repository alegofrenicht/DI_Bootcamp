# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

some_set = {1, 2, 3, 4}
number_1 = 5
number_2 = 6
some_set.add(number_1)
some_set.add(number_2)
some_set.discard(6)
friend_fav_numbers = {1, 3, 7, 8, 9}
our_fav_numbers = some_set.union(friend_fav_numbers)
print(our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?
tuple_one = (1, 2)
tuple_two = (2, 3)
tuple_three = tuple_one + tuple_two


# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove("Blueberries")
basket.append('Kiwi')
basket.insert(0, 'Apples')
print(basket.count('Apples'))
basket.clear()
print(basket)


# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# float = 15.0; integer = 15
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
sequence = [1.5]
for number in range(6):
    if type(sequence[-1]) == float:
        sequence.append(int(sequence[-1] + 0.5))

    else:
        sequence.append(sequence[-1] + 0.5)


# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

loop = []
for num in range(1, 21):
    loop.append(num)

for num in range(20):
    if num % 2 == 0:
        print(loop[num])
    else:
        continue


# Exercise 6: While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

my_name = 'A'
name = input('your name: ')
while my_name != name:
    name = input('your name: ')

#
# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

fr_request = input('write down your favourite fruits ')
fruits = fr_request.split(' ')
name_fruit = input('mention any fruit ')

if name_fruit in fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')


# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings_list = []
toppings_query = input('What toppings you would like to have on your pizza? ')
toppings_list.append(toppings_query)
print('I\'ll add that topping to your pizza.')
while toppings_query != 'quit':
    toppings_query = input('What toppings you would like to have on your pizza? ')
    if toppings_query == 'quit':
        continue
    else:
        print('I\'ll add that topping to your pizza.')
        toppings_list.append(toppings_query)

toppings = ' and '.join(toppings_list)
print(f'Your pizza with {toppings} will cost {10 + len(toppings_list) * 2.5}')

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.
#
# Store the total cost of all the family’s tickets and print it out.
#
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

cost = 0
group = int(input('How many persons are you?\n'))

for member in range(group):
    question = int(input('How old are you?\n'))
    if question < 3:
        continue
    elif 3 <= question <= 12:
        cost += 10
    else:
        cost += 15

print(f'For your family it would cost {cost}')

cost = 0
teenagers = input('write your names:\n').split(', ')
for member in teenagers:
    question = int(input(f'How old are you, {member}?\n'))
    if question < 3:
        continue
    elif 3 <= question <= 12:
        cost += 10
    elif 16 < question < 21:
        print(f'{member} you\'re not allowed to go')
        teenagers.remove(member)
    else:
        cost += 15

print(f'Guys, it would cost for you {cost}')



# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
#
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []
for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f'{sandwich} is ready')



# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
print('Sorry, we ran out of pastrami, pastrami sandwich is on stop-list')
while 'Pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('Pastrami sandwich')
print('Welcome to subway!')
