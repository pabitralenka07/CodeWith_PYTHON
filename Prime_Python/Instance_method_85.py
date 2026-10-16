class Laptop:
    storage_type = "SSD"
    
    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
        
    def get_info(self): #Instance method
        print(f"Laptop has {self.RAM} RAM and {self.storage} {self.storage_type} storage.")
        
L1 = Laptop("16GB","512GB")
L2 = Laptop("8GB","256GB")

L1.get_info()
