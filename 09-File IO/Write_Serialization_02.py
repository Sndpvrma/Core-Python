import pickle

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(self.make, self.model, self.year)

with open("C:/Users/Sandeep/Desktop/New folder/Serialization_02.txt", "wb") as file:
    Cars = Car("Tata", "Seirra", 2025)
    pickle.dump(Cars, file)

print("Serialization done.")