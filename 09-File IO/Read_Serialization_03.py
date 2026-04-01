import pickle

from Write_Serialization_03 import farming

with open("C:/Users/Sandeep/Desktop/New folder/Serialization_03.txt", 'rb') as file:
    obj = pickle.load(file)
    print("Printing Farming information after unpickling")

obj.display()