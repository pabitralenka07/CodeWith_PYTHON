class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance  #Private - data mangling
        
    def get_balance(self): #Getter
        return self.__balance
    
    def set_balance(self,newBalance):   #Setter
        self.__balance = newBalance
        
acc1 = BankAccount("Ruturaj",9_87_600)

acc1.set_balance(200000)

print(acc1.name,acc1.get_balance())

print(acc1.name,acc1._BankAccount__balance) #We can also call by this .
