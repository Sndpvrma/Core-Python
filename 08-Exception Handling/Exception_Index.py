# fruits = ["apple", "banana", "cherry"]
#
# try:
#     print(fruits[4])
# except IndexError as e:
#     print('IndexError:', e)

list = ["Python", "Java", "C++"]
try:
    print(list[1])
    print(list[5])

except IndexError as e:
    print("IndexError", e)