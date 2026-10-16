class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, grade):
        self.grade = grade

class TeachingAssistant(Teacher, Student):
    def __init__(self, salary, grade ,name):
        super().__init__(salary)
        Student.__init__(self, grade)
        self.name = name

ta1 = TeachingAssistant(30000, "A", "Alice")
print(ta1.name, ta1.salary, ta1.grade)
