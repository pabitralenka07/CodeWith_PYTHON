class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

class Robot:
    def speak(self):
        print("Beep Boop")

def make_it_speak(entity):
    entity.speak()

d = Dog()
c = Cat()
r = Robot()

for e in [d, c, r]:
    make_it_speak(e)
    