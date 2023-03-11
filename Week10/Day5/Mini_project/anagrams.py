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

from anagram_checker import AnagramChecker


def main():
    while menu() != '0':
        word = input("\nEnter a word: ").strip()
        print(f'YOUR WORD: "{word.upper()}" ')
        anagram_checker = AnagramChecker(word)
        if anagram_checker.is_valid_word():
            print('This is a valid English word.')
            anagrams = anagram_checker.get_anagrams()
            print(f"Anagrams for your word: {', '.join(anagrams)}.")

        else:
            print("Word you've entered is invalid")

    exit('Come back again. Bye!')


def menu():
    return input('\nMenu:\n(1) Enter a word to find anagrams\n(0) Exit\n\nChoose the option (press the button fitting'
                 ' to the number of option and press ENTER): ')


main()
