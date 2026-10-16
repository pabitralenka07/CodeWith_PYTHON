class BankAccount:
    def __init__(self, account_no, owner_name, balance):
        self.account_no = account_no
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def check_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(101, "Pabitra", 1000)

acc.deposit(500)
acc.withdraw(300)
acc.check_balance()
