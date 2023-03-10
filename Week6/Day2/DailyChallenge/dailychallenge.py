# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
#
# Then, print the first and last characters of the given text.
#
# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World
#
#
# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
#
# Hlrolelwod
import random

str_input = input('write string ')
if len(str_input) > 10:
    print('string too long')
elif len(str_input) < 10:
    print('string not long enough')


print(str_input[0], str_input[-1])
new_string = ''
for letter in str_input:
    new_string += letter
    print(new_string)
