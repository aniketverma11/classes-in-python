class MyEditor:
    def __init__(self):
        print("compiling")
        print("Interpreting")

class Enviorment(MyEditor):
    def execute(self):
        super().__init__()
        print("Cloud computing")
        print("Enviorment setup")
        print("100 Days of code")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = Enviorment()
o1 = Laptop()
o1.code(ide)
