class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def display(self):
        print("Grandfather Name is", self.grandfathername)

class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        super().__init__(grandfathername)  # Call constructor of the Grandfather class

    def display1(self):
        print(self.fathername, "is son of", self.grandfathername)

class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        super().__init__(fathername, grandfathername)  # Call constructor of the Father class

    def displaydata(self):
        print("Son Name:", self.sonname)
        print("Father Name:", self.fathername)
        print("Grandfather Name:", self.grandfathername)

s1 = Son("Hardik", "Kunal", "Rohit")
s1.displaydata()
