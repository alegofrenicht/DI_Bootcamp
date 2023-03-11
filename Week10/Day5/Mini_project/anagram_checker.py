# Instructions
# First Download this text file : right click –> Save As
#
# 1. Create a new file called anagram_checker.py which contains a class called AnagramChecker.
#
# 2. The class should have the following methods:
#    - __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.
#    - is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.
#
#    - get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)
#
#    - Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.
#
#    - Note: None of the methods in the class should print anything.
#
# 3. Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.
#
# 4. It should do the following:
#    1. Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
#    2. If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
#       - Only a single word is allowed. If the user typed more than one word, show an error message.
#       (Hint: how do we know how many words were typed?)
#       - Only alphabetic characters are allowed. No numbers or special characters.
#       - Whitespace should be removed from the start and end of the user’s input.
#
# 3. Once your code has decided that the user’s input is valid, it should find out the following:
#    - All possible anagrams to the user’s word.
#    - Create an AnagramChecker instance and apply it to the steps created above.
#    - Display the information about the word in a user-friendly, nicely-formatted message such as:
#
#           YOUR WORD :”MEAT”
#           this is a valid English word.
#           Anagrams for your word: mate, tame, team.

class AnagramChecker:
    def __init__(self, user_word: str):
        with open('sowpods.txt', encoding='utf-8') as f:
             self.file = f.read().split('\n')
        self.user_word = user_word.lower()

    def is_valid_word(self):
        if self.user_word.strip().isalpha() and self.user_word.upper() in self.file:
            return True
        else:
            return False



    def get_anagrams(self):
        word_voc = {}
        anagrams = []
        for letter in sorted(self.user_word.lower()):
            word_voc[letter] = word_voc.get(letter, 0) + 1
        for word in self.file:
            file_word = {}
            for letter in sorted(word.lower()):
                file_word[letter] = file_word.get(letter, 0) + 1
            if file_word == word_voc and word.lower() != self.user_word:
                anagrams.append(word)
        return anagrams


