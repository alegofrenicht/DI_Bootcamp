# Instructions
# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples
#
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
#
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
#
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

number = int(input('choose number:\n'))
length = int(input('choose length:\n'))
numbers = []
for num in range(1, length + 1):
    numbers.append(number * num)
print(numbers)



# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples
#
# user's word : "ppoeemm" ➞ "poem"
#
# user's word : "wiiiinnnnd" ➞ "wind"
#
# user's word : "ttiiitllleeee" ➞ "title"
#
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

string = input('enter your word:\n')

for i in range(len(string) - 1):
    if string[i] == string[i + 1]:
        string = string.replace(string[i], ' ', 1)
print(''.join(string.split(' ')))

# or another a little more sophisticated solution:

# string = input('enter your word:\n')
# string = ''.join(sorted(set(string), key=string.index))
# print(string)

