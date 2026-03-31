# my_list = [1,2,3]
# iterator=iter(my_list)
#
# try:
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
#     print(next(iterator))
# except StopIteration:
#     print("List End")

list1 = ["mango", "banana", "cherry"]

iterator = iter(list1)

try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("List End")