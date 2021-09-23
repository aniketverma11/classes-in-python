from threading import *
from time import *


class top(Thread):
    def run(self):
        for i in range (5):
            print("Hello")
            sleep(1)


class down(Thread):
    def run(self):
        for i in range (5):
            print("World")
            sleep(1)


onj = top()
obj = down()

onj.start()
sleep(0.2)
obj.start()
