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

class Text:
    def __init__(self, txt):
        self.txt = txt

    def 