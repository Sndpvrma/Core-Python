# Inherit Thread class and override run() method

import threading
from threading import *

class Hello(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(0,15):
            print(self.name, i)

t1 = Hello("Warner")
t2 = Hello("Smith")

t1.start()
t2.start()