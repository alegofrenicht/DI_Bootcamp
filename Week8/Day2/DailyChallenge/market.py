class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal, number=1):
        self.animals[animal] = self.animals.get(animal, 0) + number




    def get_info(self):
        print(f"{self.name}' farm\n")
        [print(f"{key} : {value}") for key, value in self.animals.items()]
        return '\n\tE-I-E-I-0!'

    def get_animal_types(self):
        animal_types = []
        [animal_types.append(type) for type in sorted(self.animals)]
        return animal_types

    def get_short_info(self):
        animals = self.get_animal_types()
        return f"McDonald’s farm has {animals[0]}s, {animals[1]}s and {animals[2]}."



macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())
