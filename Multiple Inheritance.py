class Father:
    def __init__(self, fathername):
        self.fathername = fathername

    def display(self):
        print("Father name is:", self.fathername)

class Mother:
    def __init__(self, mothername):
        self.mothername = mothername

    def display1(self):
        print("Mother name is:", self.mothername)

class Son1(Father, Mother):
    def __init__(self, sonname, fathername, mothername):
        super().__init__(fathername)
        Mother.__init__(self, mothername)
        self.sonname = sonname

    def displaydata(self):
        print(self.sonname, "is son of", self.fathername, "and", self.mothername)

s1 = Son1("Hardik", "Pandya", "Poonam")
s1.displaydata()
