# 🌟 Exercise 1 : Human
# Instructions
# Create a class Human, it has the following attributes:
# name (str)
# age (int)
# living_place (Building - Default is None)
#
# Create another class Building, it has the following attributes:
# address (str)
# inhabitants (List of Human objects - Default is empty)
#
# Create a class City, it has the following attributes:
# name (str)
# buildings (List of Building objects - Default is empty)
#
# Add the move(self, building) method to the Human class, it sets the living place of this human to the building and add this human to the building inhabitants.
# Add the construct(self, address) method to the City class, it adds a building at the referenced address.
# Add the info(self, address) method to the City class, it displays the number of buildings and the mean age of the citizens.
# Created objects and call the methods


class Human:
    def __init__(self, name: str, age: int, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def __str__(self):
        return f"{self.name}, {self.age}"

    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)


class Building:
    def __init__(self, address: str):
        self.address = address
        self.inhabitants = []
        self.mean_age = 0

    def __str__(self):
        return f"{self.address}"

    def all_inhabitants(self):
        for inhabitant in self.inhabitants:
            print(inhabitant)

    def mean_age_func(self):
        sum_age = 0
        for inhabitant in self.inhabitants:
            sum_age += inhabitant.age
        self.mean_age = sum_age / len(self.inhabitants)


class City:

    def __init__(self, name: str):
        self.name = name
        self.buildings = {}

    def construct(self, address):
        self.buildings[f"{address}"] = Building(address)

    def info(self, address):
        if address in self.buildings:
            self.buildings[address].mean_age_func()
            print(f'In building on "{address}" live {len(self.buildings[address].inhabitants)}'
                  f' citizen/-s and their mean age is {int(self.buildings[address].mean_age)}')
        else:
            print('Not found')


John = Human('John Weak', 35)
Max = Human('Max Payne', 20)
Hannah = Human('Hannah Montana', 15)
new_york = City('New York')
new_york.construct('Hyde Park, 35')
new_york.construct('Baker street, 10')
Max.move(new_york.buildings['Hyde Park, 35'])
Hannah.move(new_york.buildings['Hyde Park, 35'])
John.move(new_york.buildings['Hyde Park, 35'])
new_york.info('Hyde Park, 35')
