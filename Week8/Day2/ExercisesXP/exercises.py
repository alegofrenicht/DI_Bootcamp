# 🌟 Exercise 1: Cats
# Instructions
# Using this class
#
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# 1. Instantiate three Cat objects using the code provided above.
# 2. Outside of the class, create a function that finds the oldest cat and returns the cat.
# 3. Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cats = []
cat_one = Cat('Max', 1)
cats.append(cat_one)
cat_two = Cat('Rain', 2)
cats.append(cat_two)
cat_three = Cat('Dog', 1)
cats.append(cat_three)


def oldest_cat(cats):
    oldestCat = ['', 0]
    for cat in cats:
        if cat.age > oldestCat[1]:
            oldestCat = [cat.name, cat.age]
    return oldestCat


print(f"The oldest cat is {oldest_cat(cats)[0]}, and is {oldest_cat(cats)[1]} years old.")


# 🌟 Exercise 2 : Dogs
# Instructions
# 1. Create a class called Dog.
# 2. In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# 3. Create a method called bark that prints the following string “<dog_name> goes woof!”.
# 4. Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# 5. Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# 6. Print the details of his dog (ie. name and height) and call the methods bark and jump.
# 7. Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# 8. Print the details of her dog (ie. name and height) and call the methods bark and jump.
# 9. Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")

    def jump(self):
        print(f"{self.name} jumps {self.height * 2} cm high!")



davids_dog = Dog('Rex', 50)

print(f"Name: {davids_dog.name}\nHeight: {davids_dog.height}")
davids_dog.jump()
davids_dog.bark()

sarahs_dog = Dog('Teacup', 20)
print(f"Name: {sarahs_dog.name}\nHeight: {sarahs_dog.height}")
sarahs_dog.jump()
sarahs_dog.bark()

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger dog")
else:
    print(f"{sarahs_dog.name} is bigger dog")


# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# 1. Define a class called Song, it will show the lyrics of a song.
#    Its __init__() method should have two arguments: self and lyrics (a list).
# 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# 3. Create an object, for example:
#
#    stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
#
#
# 4. Then, call the sing_me_a_song method. The output should be:
#
#    There’s a lady who's sure
#    all that glitters is gold
#    and she’s buying a stairway to heaven

class Song:

    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        [print(line) for line in self.lyrics]

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Instructions
# 1. Create a class called Zoo.
# 2. In this class create a method __init__ that takes one parameter: zoo_name.
#    It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# 3. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# 4. Create a method called get_animals that prints all the animals of the zoo.
# 5. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# 6. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
#    Example
#
# {
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }
#
#
# 7. Create a method called get_groups that prints the animal/animals inside each group.
#
# 8. Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
#   Which animal should we add to the zoo --> Giraffe
#   x.add_animal(Giraffe)

class Zoo:

    def __init__(self, zoo_name):
        self.animals = []
        self.zoo_name = zoo_name

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        [print(animal, end=' ') for animal in self.animals]

    def sell_animals(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):
        group_of_animals = {}
        count = 0
        for animal in sorted(self.animals):
            if animal[0] not in list(map(lambda x: x[0][0], group_of_animals.values())):
                count += 1
                group_of_animals[count] = [animal]

            else:
                group_of_animals[count].append(animal)
                group_of_animals[count].sort()

        self.animals = group_of_animals

    def get_groups(self):
        for group in self.animals:
            group_name = f'Group number {group}: '
            group_name += ', '.join(self.animals[group])
            print(group_name)


ramat_gan_safari = Zoo('Ramat Gan Safari')
ramat_gan_safari.add_animal('Ape')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.add_animal('Cougar')
ramat_gan_safari.add_animal('Emu')
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Baboon')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
