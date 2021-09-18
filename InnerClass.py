class Student:

    def __init__(self, name, rollno):

        self.name = name 
        self.rollno = rollno
        self.lap = self.Laptop()


    def show(self):
        print(self.name, self.rollno)
        self.lap.show()
    class Laptop:

        def __init__(self):
            self.lap = "Dell"
            self.ram = 8
            self.proessor = "i3"

        def show(self):
            print(self.lap, self.ram, self.proessor)


p1 =  Student("Aniket", 10)
p2 = Student("Aryan", 18)
p1.show()

print(id(p1))
print(id(p2))