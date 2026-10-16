class Product:
    def __init__(self,name,price):
        self.name =name
        self.price = price
        
    def get_info(self):
        print(f"Price of {self.name} is Rs. {self.price}")
        
p1 = Product("Apple","67,999")
p2 = Product("Vivo","35,999")
p3 = Product("Nokia","7,999")

p3.get_info()
