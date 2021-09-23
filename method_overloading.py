#Method overloading
#basically in python there is no any type of method overloading concept like c++ and java
#so we do somthing to make Method overloading
class A:

    def __init__(self, i, j ):
        self.i = i 
        self.j = j

    def avg(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return (a+b+c)/2

        elif a!=None and b!=None and c==None:
            return (a+b)/2

        else:
            return a        

obj = A(5,6)
print((obj.avg(2)))        