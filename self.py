class Computer:

    def __init__(self):
        self.age = 18
        self.name = 'Aniket'

    def update(self):
        self.age = 21
        

    def compare(self,other):
        if self.age == other.age:
            return True

        else:
            return False


p1 = Computer()
p2 = Computer()
p1.update()
if p1.compare(p2):
    print('They are same')
else:
    print('They are diffrent')



