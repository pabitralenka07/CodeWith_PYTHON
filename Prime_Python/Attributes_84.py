class Student:
    college_name = "IIT Kharagpur" #Class attribute
    
    def __init__(self, name, cgpa):
        self.name = name #Instance attribute
        self.cgpa = cgpa
        
stu1 = Student("Rahul", 7.8)
print(stu1.name) #stu1 is an object of Student class

print(stu1.college_name)
print(Student.college_name)
