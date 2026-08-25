class Student:
    def __init__(self, marks):
        self.marks = marks
    
    def get_marks(self):
        return self.marks 
    
    def set_marks(self, new_marks):
        if 0<=new_marks<=100:
            self.marks = new_marks
        else:
            print("INVALID MARKS")

s1 = Student(85)

s1.set_marks(95)

print(s1.get_marks())