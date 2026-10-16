class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
        
    def get_cgpa(self):
        return self.cgpa
    
stu1 = Student("Rahul",7.8)
stu2 = Student("PAbitra",8.3)
stu3 = Student("Rashi",4.8)

print(stu2.get_cgpa())
print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")
