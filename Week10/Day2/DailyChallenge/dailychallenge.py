from translate import Translator
# Instructions :
# Look at this result :
# {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# You have to recreate the result using a translator module.

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
vocabulary = {}
translator = Translator(from_lang='fr', to_lang="en")
for word in french_words:
    vocabulary[word] = translator.translate(word)
print(vocabulary)
