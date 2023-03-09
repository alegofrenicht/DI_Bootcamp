# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”
#
# 1. Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
#
# 2. Implement the following methods:
#       - a method to return the frequency of a word in the text (assume words are separated by whitespace)
#         return None or a meaningful message.
#       - a method that returns the most common word in the text.
#       - a method that returns a list of all the unique words in the text.
# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
#
# 1. Implement a classmethod that returns a Text instance but with a text file:
#
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
#
#
# 2. Now, use the provided the_stranger.txt file and try using the class you created above.

import string


class Text:
    def __init__(self, txt: str):
        self.txt = txt
        self.nopunc_txt = self.txt.translate(str.maketrans('', '', string.punctuation)).lower().strip().split(' ')

    def word_frequency(self, word):
        words = self.nopunc_txt.count(word.lower())
        if words == 0:
            return None
        elif words == 1:
            return f"Word '{word}' appears {words} time in the text"
        else:
            return f"Word '{word}' appears {words} times in the text"

    def most_common(self):
        times = 0
        mst_cmn_word = ''
        for word in self.nopunc_txt:
            num_words = self.nopunc_txt.count(word)
            if num_words > times:
                times = num_words
                mst_cmn_word = word
        return f"The most common word in the text: '{mst_cmn_word}'"

    def unique_words(self):
        unique_words = []
        for word in self.nopunc_txt:
            num_words = self.nopunc_txt.count(word)
            if num_words == 1:
                unique_words.append("'" + word + "'")
        return f"Unique words: {', '.join(unique_words)}"

    @classmethod
    def from_file(cls, file_text):
        with open(file_text) as f:
            some = f.read().split('\n')
        return cls(' '.join(some))


simple_string = Text('A good book would sometimes cost as much as a good house.')
print(simple_string.word_frequency('book'))
print(simple_string.most_common())
print(simple_string.unique_words())
stranger = Text.from_file('the_stranger.txt')
