#Method Overriding

class math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def cal(self):
        return self.a+self.b


class Mathematic(math):
    def cal(self):
        return self.a*self.b



obj = math(5,6)
print(obj.cal())