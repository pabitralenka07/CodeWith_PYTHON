class Employee:
    start_time = "9:00"
    end_time = "5:00"
    
    def change_time(self, new_end_time):
        self.end_time = new_end_time
        
class Administrator(Employee):
    def __init__(self, role):
        self.role = role

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
            
staff1 = Administrator("HR")
staff2 = Teacher("Math")

print(staff1.role, staff1.start_time, staff1.end_time)
print(staff2.subject, staff2.start_time, staff2.end_time)
