import pickle

from Write_serialization import Student

with open("C:/Users/Sandeep/Desktop/New folder/write_serialization.txt", 'rb') as file:
    obj = pickle.load(file)
    print("Printing Student Information after unpickling")

obj.display()