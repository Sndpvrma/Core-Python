# With Treads

import threading
# from threading import *

def hello():
    for i in range(0,12):
        print("Hello World", i)

def hi():
    for i in range(0,12):
        print("Hello Python", i)

t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hi)

t1.start()
t2.start()