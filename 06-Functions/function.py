def greeting():
    print("Hello! Kaise ho?")

greeting()

def say_hello(naam):
    print("Hello", naam)

say_hello("Amit")

def add(a, b):
    return a + b

result = add(5, 10)
print("Sum is:", result)

naam = "Python"
print(len(naam)) # len() ek built-in function hai jo length batata hai ki usme total kitne akshar ya number hai.

def square(n):
    return n * n

print(square(6))

# Syntax: lambda arguments : expression
multiply = lambda x, y : x * y

print(multiply(7, 6))