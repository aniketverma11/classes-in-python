class CarCompany(): #this is parent class basically called Base class and use to being inherited from.
    
    def __init__(self, ModelID, ModelName):
        self.ModelID = ModelID
        self.ModelName = ModelName

    
class customer(CarCompany): #this is child class in this we are inherited the parent class and reuse the instances from parents
    def __init__(self, ModelID, ModelName, customerName, customerAge):
        super().__init__(ModelID, ModelName)
        self.customerName = customerName
        self.customerAge = customerAge

    def printl(self):
        print(f"The new car in available in showroom which has ID no. is {self.ModelID} and the name is {self.ModelName}.")
        print(f"The Name of customer who seeks to purchase this car is {self.customerName} and he is able to take this car because his age is {self.customerAge} ")
        
p1 = customer(55686, "suzuki I20", "Abishek", 21)
p1.printl()
