# Without threading

def Hello():
    for i in range(2,25,3):
        print("Python", i)

def Hi():
    for i in range(1,24,3):
        print("Java", i)

Hello()
Hi()