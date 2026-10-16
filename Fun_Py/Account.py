import random
import string
import random
import string

class BankAccount:
    def __init__(self,name,adhara):
        self.adhara=adhara
        self.name=name
        self.account_number = self._generate_account_number
        self.balance = 0
        self.transaction_history = []
        self.password = self._generate_password()

    def _generate_password(self, length=15):
        characters =  string.digits
        password="name"+characters
        return ''.join(random.choice(characters) for i in range(length))
    
    def _generate_account_number(self,length=10):
        number=adhara_no
        return ''.join(random.choice(adhara_no)for i in range(length))

    def get_password(self):
        return self.password

    def credit(self, amount):
        if amount <= 0:
            raise ValueError("Credit amount must be positive.")
        self.balance += amount
        self.transaction_history.append(f"Credited ${amount}")
        print(f"The New balance is: ${self.balance}")

    def debit(self, amount):
        if amount <= 0:
            raise ValueError("Debit amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transaction_history.append(f"Debited ${amount}")
        print(f"The New balance is: ${self.balance}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

if __name__ == "__main__":
    print("Hii...you are welcome to our bank:")
    #print("\n")
    print("To create a bank account we need your adhara number and your name:")
    adhara_no=input("enter your Adhara number:")
    name=input("Enter your name:")
    account = BankAccount(name,adhara_no)
    
    print(f"Account password is: {account.get_password()}") 
    print(f"Account number is: {account._generate_account_number()}") # Display the generated password
    #amount=int(input("enter the withdraw amount:"))
    account.credit(int(input("enter your deposit amount:"))) 
    amount=int(input("enter the withdraw amount:"))# Deposit $100
    account.debit(amount)  
    #account.credit(input("enter your deposit amount:")) # Withdraw $50
    #try:
        # account.debit(amount)   # Attempt to withdraw more than the balance
    #except ValueError as e:
        # print(e)
    
    print(f"Final balance: ${account.get_balance()}.")
    print("Transaction History:", account.get_transaction_history())

