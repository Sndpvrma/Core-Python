import pickle

class farming:
    def __init__(self, Fruits, Vegetables, Grain ):
        self.Fruits = Fruits
        self.Vegetables = Vegetables
        self.Grain = Grain

    def display(self):
        print(self.Fruits, self.Vegetables, self.Grain)

with open("C:/Users/Sandeep/Desktop/New folder/Serialization_03.txt", "wb") as file:
    Farm = farming("Apple, Banana\n", "Patato, Tomato\n", "Wheat, Rice")
    pickle.dump(Farm, file)

print("Serialization Done")
