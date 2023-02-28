class Character:
    def __init__(self, name, life=20, attack=10):
        self.name = name
        self.life = life
        self.attack = attack
        if self.life <= 0:
            print(f"{self.name} has fallen in battle. Game over")

    def basic_attack(self, other_char):
        other_char.life -= self.attack


class Druid(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print('Nature is not for the weak')

    def meditate(self):
        self.life += 10
        self.attack -= 2

    def animal_help(self):
        self.attack += 5

    def fight(self, other_char):
        other_char.life -= (self.life * 0.75 + self.attack * 0.75)


class Warrior(Character):

    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print('Call me Juggernaut')

    def brawl(self, other_char):
        other_char.life -= 2 * self.attack
        self.life += 0.5 * self.attack

    def train(self):
        for attribute in [self.life, self.attack]:
            attribute += 2

    @staticmethod
    def roar(other_char):
        other_char.attack -= 3


class Mage(Character):
    def __init__(self, name, life=20, attack=10):
        super().__init__(name, life, attack)
        print('There is purity in silence!')

    @staticmethod
    def curse(other_char):
        other_char.attack -= 2

    def summon(self, amount=1):
        for time in range(amount):
            self.attack += 3

    def cast_spell(self, other_char):
        other_char.life -= self.attack / self.life


lone_druid = Druid('Lone Druid', 300, 40)
silencer = Mage('Silencer', 160, 35)
juggernaut = Warrior('Juggernaut', 200, 55)











