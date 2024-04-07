class Student:
    def __init__(self,rno,name):
        self.rno=rno
        self.name=name
    def display(self):
        print("Rno : ",self.rno)
        print("Name : ",self.name)

s1 = Student(1,"Mohan")
s1.display()
