class Computer:
    def __init__(self,mno,cpu):
        self.mno = mno
        self.cpu = cpu

    def config(self):
        print('Config is.',self.mno,self.cpu)

a = Computer('Dell', 'i3')
a.config()