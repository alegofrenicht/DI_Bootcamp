# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator.
# We will do this by asking the user how long the sentence should be and then printing the generated sentence.
#
# Hint : The generated sentences do not have to make sense.
#
# 1. Download this word list
#
# 2. Save it in your development directory.
#
# 3. Create a function called get_words_from_file. This function should read
# the file’s content and return the words as a collection. What is the correct data type to store the words?
#
# 4. Create another function called get_random_sentence which takes a single parameter called length.
# The length parameter will be used to determine how many words the sentence should have. The function should:
#   - use the words list to get your random words.
#   - the amount of words should be the value of the length parameter.
#
# 5. Take the random words and create a sentence (using a python method), the sentence should be lower case.
#
# 6. Create a function called main which will:
#
#    1. Print a message explaining what the program does.
#
#    2. Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20.
#       Validate your data and test your validation!
#         - If the user inputs incorrect data, print an error message and end the program.
#         - If the user inputs correct data, run your code.

import random

def get_words_from_file():
    with open('sowpods.txt', encoding='utf-8') as f:
        return f.read().split('\n')

def get_random_sentence(length):
    random_words = []
    for i in range(length):
        random_words.append(random.choice(get_words_from_file()))
    return ' '.join(random_words).lower().capitalize()

def main():
        num_request = input("Please choose the length of sentence you want to generate (from 2 to 20 words): ")
        if not num_request.isdigit():
            raise Exception("Unaccepted type of request")
        if 1 < int(num_request) < 21:
            print(get_random_sentence(int(num_request)))
        else:
            print('Wrong number')
            return

main()



