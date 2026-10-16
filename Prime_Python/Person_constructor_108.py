class Person:
    def __init__(self, name, age = None ,address = None):
        self.name = name
        self.age = age
        self.address = address

    def Display(self):
        print("Name : " , self.name)
        
        if self.age is not None:
            print("Age : " , self.age)
        if self.address is not None:
            print("Address : " , self.address)

p1 = Person("Alice")
p2 = Person("Bob", 30)
p3 = Person("Charlie", 25, "123 Main St")

p1.Display()
print()
p2.Display()
print()
p3.Display()
