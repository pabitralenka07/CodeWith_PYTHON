class Employee:
    start_time = "9:00"
    end_time = "5:00"

class Administrator(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(Administrator):
    def __init__(self, salary, role):
        self.salary = salary
        super().__init__(role)

acc1 = Accountant(50000, "Finance")
print(acc1.salary, acc1.role, acc1.start_time, acc1.end_time)
