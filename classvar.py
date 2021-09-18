class Car:

    wheel = 4#this is class variable
    def __init__(self, ml, avg):
        self.ml = ml
        self.avg = avg
    
    @classmethod#this is the class method that can be make non instance method that can not be change
    def whl(cls):
        cls.wheel = 6 
        

p1 = Car(5, 6)
Car.wheel
print(p1.ml, p1.avg, Car.wheel)