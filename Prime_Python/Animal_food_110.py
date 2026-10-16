class Herbivore:
    def eat_plants(self):
        print("Eats plants")

class Carnivore:
    def eat_meat(self):
        print("Eats meat")

class Omnivore:
    def eat_all(self):
        print("Eats both plants and meat")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Bear name:", self.name)

b = Bear("Baloo")

b.show()
b.eat_plants()
b.eat_meat()
b.eat_all()
