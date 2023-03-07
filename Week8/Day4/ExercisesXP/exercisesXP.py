# 🌟 Exercise 1 : Pets
# Instructions
# Using this code:
# 1. Create another cat breed named Siamese which inherits from the Cat class.
# 2. Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# 3. Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# 4. Take all the cats for a walk, use the walk method.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'

all_cats = [Chartreux('A', 1), Siamese('B', 2), Bengal('C', 3)]
sara_pets = Pets(all_cats)
sara_pets.walk()


# 🌟 Exercise 2 : Dogs
# Instructions
# 1. Create a class called Dog with the following attributes name, age, weight.
# 2. Implement the following methods in the Dog class:
#   - bark: returns a string which states: “<dog_name> is barking”.
#   - run_speed: returns the dogs running speed (weight/age*10).
#   - fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
#
# 3. Create 3 dogs and run them through your class.

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return int(self.weight / self.age * 10)

    def fight(self, other_dog):
        if other_dog.run_speed() * other_dog.weight > self.weight * self.run_speed():
            return f"{other_dog.name} is the winner"

        return f"{self.name} is the winner"

dog_one = Dog('One', 2, 15)
dog_two = Dog('Two', 1, 25)
dog_three = Dog('Three', 5, 20)

print(dog_one.fight(dog_two))
print(dog_three.fight(dog_one))
print(dog_two.fight(dog_three))


# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# 1. Create a new python file and import your Dog class from the previous exercise.
# 2. In the new python file, create a class named PetDog that inherits from Dog.
# 3. Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# 4. Add the following methods:
#    - train: prints the output of bark and switches the trained boolean to True
#    - play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
#    - do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#       -“dog_name does a barrel roll”.
#       -“dog_name stands on his back legs”.
#       -“dog_name shakes your hand”.
#       -“dog_name plays dead”.      -

# !!! let's say I created a new file and imported Dog class from this file doing this:
#    <<<<from exercisesXP import Dog>>>>
from random import randint


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, dogs):
        dogs = ', '.join(dogs)
        print(f"{dogs} all play together")

    def do_a_trick(self):
        tricks = [f"{self.name} does a barrel roll", f"{self.name} stands on his back legs",
                  f"{self.name} shakes your hand", f"{self.name} plays dead"]
        if self.trained:
            print(tricks[randint(0, 3)])
        else:
            print(f"{self.name} stares at you smiling")

john_dog = PetDog('John', 2, 10)
john_dog.train()
john_dog.do_a_trick()
