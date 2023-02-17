# Instructions
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# Use List Comprehension
# Example:
#
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world

sequence = input('enter line of words separated with commas:\n')
print(','.join(sorted(sequence.split(','))))
