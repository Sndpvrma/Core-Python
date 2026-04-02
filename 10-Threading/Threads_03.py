# Parameterized function as thread

import threading

def hello(name):
    for i in range(0,12):
        print(name, i)

t1 = threading.Thread(target=hello, args=("Raju",))
t2 = threading.Thread(target=hello, args=("Shyam",))

t1.start()
t2.start()