import pickle

with open("C:/Users/Sandeep/Desktop/New folder/Serialization_02.txt", "rb") as file:
    obj = pickle.load(file)
    print("Printing Car Information after unpickling")

obj.display()
