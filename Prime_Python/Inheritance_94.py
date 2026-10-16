class Employee:
    start_time = "9:00"
    end_time = "5:00"
    
    def change_time(self, new_end_time):
        self.end_time = new_end_time
        
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
            
t1 = Teacher("Math")

t1.change_time("6:00")

print(t1.subject,t1.start_time, t1.end_time)
