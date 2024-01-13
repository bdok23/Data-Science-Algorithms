class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) # same as lines 3 and 4
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    #If you add a method in the child class with the same name as a function in the parent class, 
    # the inheritance of the parent method will be overridden.

x = Student("James", "Smith", 2018)

x.printname()
x.welcome()