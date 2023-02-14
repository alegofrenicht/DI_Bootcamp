# 🌟 Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
voc = {}
for key, value in zip(keys, values):
    voc[key] = value


# 🌟 Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Given the following object:
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
#
# How much does each family member have to pay ?
#
# Print out the family’s total cost for the movies. Bonus: Ask the user to input the names and ages instead of using
# the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is
# initially empty).


family = {}
while True:
    name = input('Say your names, please\n')
    if name == 'that\'s all': # here you can use double quotes then it will be: "that's all" 
        break
    age = int(input('and age\n'))
    if name == 'that\'s all':
        end = False
    else:
        family[name] = age

cost = 0
for member in family.values():
    if member < 3: # it redundant, you can remove this if condition
        continue
    elif 3 <= member <= 12:
        cost += 10
    else:
        cost += 15

print(f'Guys, it would cost for you {cost}')


# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

brand = {'name': 'Zara', 'creation_date': 1975, 'creator_name': 'Amancio Ortega Gaona',
         'type_of_clothes': ['men', 'women', 'children', 'home'],
         'international_competitors': ['Gap', 'H&M', 'Benetton'], 'number_stores': 2, 'major_color': {'France': 'blue',
                                                                                                      'Spain': 'red',
                                                                                                      'US': ['pink',
                                                                                                             'green']}}

# 3. Change the number of stores to 2.

# 4. Print a sentence that explains who Zaras clients are.

clients = brand['type_of_clothes']
print(f'Zara\'s clients are: {clients[0]}, {clients[1]}, {clients[2]}')

# 5. Add a key called country_creation with a value of Spain.

brand['country_creation'] = 'Spain'

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if 'international_competitors' in brand.keys():
    brand['international_competitors'].append('Desigual')

# 7. Delete the information about the date of creation.

del brand['creation_date']

# 8. Print the last international competitor.

print(brand['international_competitors'][-1])

# 9. Print the major clothes colors in the US.

[print(some, end=' ') for some in brand['major_color']['US']]

# 10. Print the amount of key value pairs (ie. length of the dictionary).

print(f'\n{len(brand)}')

# 11. Print the keys of the dictionary.

[print(key, end='!!!') for key in brand.keys()]

# 12. Create another dictionary called more_on_zara with the following details:
#
# creation_date: 1975
# number_stores: 10 000
#
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}

# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand.update(more_on_zara)

# 14. Print the value of the key number_stores. What just happened ?

print(f'\nnumber_stores values is: {brand["number_stores"]}')


# Exercise 4 : Disney Characters
# Instructions
# Use this list :
#
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# Analyse these results :
#
# #1/
#
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
#
# #2/
#
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#
# #3/
#
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
#
#
# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

disney_users_A = {}
for key, value in enumerate(users):
    disney_users_A[value] = key

# 2. Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

disney_users_B = {}
for key, value in enumerate(users):
    disney_users_B[key] = value

# 3. Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.

disney_users_C = {}

for key, value in zip(sorted(disney_users_A), disney_users_B):
    disney_users_C[key] = value

# 4. Only recreate the 1st result for:
#       1. The characters, which names contain the letter “i”.
#       2. The characters, which names start with the letter “m” or “p”.

disney_users_A = {}

for key, value in enumerate(users):
    if 'i' in value:
        disney_users_A[value] = key
    elif value.lower().startswith('m') or value.lower().startswith('p'):
        disney_users_A[value] = key
    else: # this else is redundant
        continue
