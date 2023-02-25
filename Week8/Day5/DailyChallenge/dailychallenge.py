# Part 1 : Quizz :
# Answer the following questions
#
# 1. What is a class?
# Answer: Template for creating objects.
# 2. What is an instance?
# Answer: Object created from class
# 3. What is encapsulation?
# Answer: It's an oop  concept. Describes the idea of wrapping data and the methods that work on data within one unit.
# 4. What is abstraction?
# Answer: Abstraction means hiding of information or abstracting away information and giving access to only what’s necessary.
# 5. What is inheritance?
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# 6. What is multiple inheritance?
# When a class is derived from more than one base class.
# 7. What is polymorphism?
# Answer: Allows us to define methods in the child class with the same name as defined in their parent class.
# 8. What is method resolution order or MRO?
# Answer: It's a method which shows the order of implementing classes' functions


# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.
#
# The requirements are as follows:
#
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random


class Card:
    def __init__(self):
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    def __init__(self):
        self.suits = Card().suit
        self.values = Card().value
        self.cards = [[value, suit] for suit in self.suits for value in self.values]

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)

    def deal(self):
        card = random.choice(self.cards)
        self.cards.remove(card)
        print(f"You've picked {card[0]} of {card[1]}")


deck_of_cards = Deck()

while True:
    start = input("Wanna toss a card? Yes or No\n").lower()
    if start != 'yes' and start != 'no':
        continue
    elif start == 'yes':
        deck_of_cards.shuffle()
        deck_of_cards.deal()
        print(f"{len(deck_of_cards.cards)} left")
    else:
        print('See you again!')
        break
