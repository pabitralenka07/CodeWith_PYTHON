class BankAccount:
    def __init__(self,name,balance):
        self.name = name #Public
        self.balance = balance
        
acc1 = BankAccount("Ruturaj",9_87_600)

print(acc1.name,acc1.balance)
