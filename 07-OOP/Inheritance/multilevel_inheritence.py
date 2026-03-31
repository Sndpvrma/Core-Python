# class Student:
#
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# class Text(Student):
#
#     def __init__(self, name, age, gender, student_class, marks):
#         super().__init__(name, age, gender)
#         self.studentClass = student_class
#         self.literature = marks['lit']
#         self.math = marks['math']
#         self.biology = marks['bio']
#         self.physics = marks['phy']
#
#
# class Mark(Text):
#     def __init__(self, name, age, gender, studentclass, marks_dict):
#         super().__init__(name, age, gender, studentclass, marks_dict)
#
#     def display(self):
#             print("\n--- Student Report ---")
#             print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}")
#             print(f"Class: {self.studentClass}")
#             total_marks = self.literature + self.math + self.biology + self.physics
#             print(f"Total Marks: {total_marks}")
#
# n = input("Name: ")
# a = input("Age: ")
# g = input("Gender: ")
# c = input("Class: ")
# print("Enter marks:")
# m_data = {
#     'lit': int(input("Literature: ")),
#     'math': int(input("Math: ")),
#     'bio': int(input("Biology: ")),
#     'phy': int(input("Physics: "))
# }
# m = Mark(n, a, g, c, m_data)
# m.display()

