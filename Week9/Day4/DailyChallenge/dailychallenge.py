# Instructions :
# 1. Create a Person class which will have three properties:
#    - Name
#    - List of foods they like
#    - List of foods they hate
#    - Note: A person can have an empty list for foods they hate and/or love.
#
# 2. In this class, create the method taste():
#    - It will take in a food name as a string.
#    - Return {person_name} eats the {food_name}.
#    - If the food is in the person’s like list, add ‘and loves it!’ to the end.
#    - If it is in the person’s hate list, add ‘and hates it!’ to the end.
#    - If it is in neither list, simply add an exclamation mark to the end.
# Examples
#
# p1 = Person("Sam", ["ice cream"], ["carrots"])
# p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
#
# p1.taste("cheese") ➞ "Sam eats the cheese!"
#
# p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

class Person:
    def __init__(self, name: str, food_love: list = None, food_hate: list = None):
        self.name = name
        self.food_love = food_love
        self.food_hate = food_hate

    def taste(self, food: str):
        person_quote = f"{self.name} eats the {food}"
        if food in self.food_love:
            person_quote += ' and loves it!'
        elif food in self.food_hate:
            person_quote += ' and hates it!'
        else:
            person_quote += '!'
        return person_quote



p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste('ice cream'))
print(p1.taste('cheese'))
print(p1.taste('carrots'))

