class Student:
    def __init__(self,name,roll_no,marks):
        self._name = name
        self._roll_no = roll_no
        self._marks = marks
    
    def set_name(self,name):
        if name != " ":
            self._name = name
            
    def get_name(self):
        return self._name
    
    def set_roll_no(self,roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
            
    def get_roll_no(self):
        return self._roll_no
    
    def set_marks(self,marks):
        if marks >= 0:
            self._marks = marks
            
    def get_marks(self):
        return self._marks

s = Student("Pabitra", 10, 80)

print(s.get_name())
print(s.get_roll_no())
print(s.get_marks())
