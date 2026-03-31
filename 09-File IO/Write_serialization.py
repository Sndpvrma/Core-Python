import pickle

class Student:
    def __init__(self, name, age, study_in):
        self.name = name
        self.age = age
        self.study_in = study_in

    def display(self):
        print(self.name, self.age, self.study_in)

with open("C:/Users/Sandeep/Desktop/New folder/write_serialization.txt", "wb") as file:
    stu = Student("Chhota Bheem", 25, "Last Year")
    pickle.dump(stu, file)

print("Serialization done.")