class Student:
    def __init__(self,name,cgpa): #Parameterized Constructor
        self.name = name
        self.cgpa = cgpa
        
stu1 = Student("Rahul",7.8)
stu2 = Student("PAbitra",8.3)
stu3 = Student("Rashi",4.8)

print(stu1.name)
print(stu2.cgpa)
print(stu3.name)
