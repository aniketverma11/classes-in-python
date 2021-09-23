class A:

    def __init__(self):
        print("Hello!World")
        self.C 

    def food(self):
        print("today i have ate 'Samosa'")

class B:

    def __init__(self):
        print("Hello! My Family") 

    def familyinfo(self):
        print("In my family has 5 members. and all are expert in their occupation")
        
class C(B,A):
    
    def __init__(self):  
        super().__init__() 
        print("Hello! Relatives")
        
p1 = C()
p1.food()
p1.familyinfo()



    