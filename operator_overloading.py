class operator:
    def __init__(self, m ,n):
        self.m = m 
        self.n = n 
#initialize the variables the we can use whole over the class

    def addition(self):
        self.c = self.m + self.n
        return self.c

    def __add__(self,other):
        m = self.m + other.m
        n = self.n + other.n
        return m,n

    def __sub__(self,other):
        m = self.m - other.m
        n = self.n - other.n
        return m,n

class operator1(operator):
    def __init__(self, m ,n):
        self.m = m 
        self.n = n 
#initialize the variables the we can use wholw over the class

    def subtraction(self):
        self.c = self.m - self.n
        return self.c


a = operator(20,6)
print(a.addition())

b = operator1(50,6)
print(b.subtraction())

print(a+b)

print(a-b)






