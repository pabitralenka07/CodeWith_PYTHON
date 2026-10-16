from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, stipend):
        self.stipend = stipend
        
    def calculate_salary(self):
        return self.stipend

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self.salary = salary
        
    def calculate_salary(self):
        return self.salary

class ContractEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate
        
    def calculate_salary(self):
        return self.hours * self.rate

i = Intern(10_000)
f = FullTimeEmployee(50_000)
c = ContractEmployee(20, 500)

print("Intern Salary:", i.calculate_salary())
print("Full-Time Salary:", f.calculate_salary())
print("Contract Salary:", c.calculate_salary())
