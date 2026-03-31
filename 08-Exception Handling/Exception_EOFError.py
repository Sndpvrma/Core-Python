# try:
#     name = input("Write your name here: ")
#     print(name)
# # dokar
# except EOFError as e:
#     print("\nError: Please written somthing  (EOF)!", e)

try:
    name = input("Enter your name: ")
    print(name)

except EOFError as e:
    print("EOFError", e)