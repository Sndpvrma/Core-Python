# student = {"name": "Rohan", "age": 25, "city": "Indore"}
#
# print(student["name"])
#
# try:
#     print(student["Roll_no"])
#
# except KeyError as e:
#     print("Key not found", e)

# NameError tab aata hai jab Python ko koi aisa
# naam (variable, function, ya class) milta hai
# jo usne pehle kabhi suna hi nahi.

try:
    print(greeting)

except NameError as e:
    print("Variable not found", e)

# -----------------------------------------------------------------

Student = {"name":"Rohan", "age":25, "City": "Indore"}
print(Student["name"])

try:
    print(Student["Roll NO"])

except KeyError as e:
    print("Key not found", e)


try:
    print(morning)

except NameError as e:
    print("Variable not found", e)

