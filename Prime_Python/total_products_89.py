class Product:
    count = 0
    
    def __init__(self,name,price):
        self.name =name
        self.price = price
        Product.count += 1
        
    def get_info(self):
        print(f"Price of {self.name} is Rs. {self.price}")
        
    @classmethod
    def total_products(cls):
        print(f"Total products in store is {cls.count}") 
    
p1 = Product("Apple","67,999")
p2 = Product("Vivo","35,999")
p3 = Product("Nokia","7,999")

Product.total_products()
