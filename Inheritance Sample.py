class Person:
    def __init__(self,eno,name):
        self.eno=eno
        self.name=name
    def display(self):
        print("Employee No. :",self.eno)
        print("Employee Name : ",self.name)
class Employee(Person):
    def callme(self):
        print("I can use my parent class variables")

P= Person(1,"Mohan")
E=Employee(2,"Ram Kumar")

print("Employee Details : ")
print("-"*25)

P.display()
E.display()
