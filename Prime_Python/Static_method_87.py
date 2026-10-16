class Laptop:
    storage_type = "SSD"
    
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
        
    @classmethod
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")
    
    def get_info(self): #Instance method
        print(f"Laptop has {self.RAM} RAM and {self.storage} {self.storage_type} storage.")
    
    @staticmethod
    def calc_discount (Price,discount):
        final_price = Price - (discount * Price/100)
        print(f"Discounted price = {final_price}")
        
L1 = Laptop("16GB","512GB")
L2 = Laptop("8GB","256GB")

L1.calc_discount(4_00_000,30)
