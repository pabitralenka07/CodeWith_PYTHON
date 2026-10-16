# Functions overriding

class Employee:
    def get_designation(self):
        print("Designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Designation = Teacher")

t1 = Teacher()
t1.get_designation()
