# NotImplementedError ek aisi exception hai jise Python tab
# raise karta hai jab koi method ya function likha toh gaya hai,
# lekin uske andar ka kaam (logic) abhi tak poora nahi kiya gaya.
# Ise aksar Object-Oriented Programming (OOP) mein "placeholder" ki
# tarah use kiya jata hai.

class Animal:
    def speak(self):
        # Humne method bana diya, par iska koi logic nahi likha
        raise NotImplementedError("Please write this method in child class")

class Dog(Animal):
    def speak(self):
        return 'Woof''Woof'

class Cat(Animal):
        pass # Cat mein humne 'speak' nahi likha

d=Dog()
print(d.speak())

c=Cat()

try:
    print(c.speak()) # Ye error dega kyunki Cat ne Animal wala method inherit kiya jo khali hai

except NotImplementedError as e:
    print("error", e)