# x=10
# try:
#     x.append(5)
#
# except AttributeError as e:
#     print("AttributeError", e)
#
# finally:
#     print("Program done")

x= 10

try:
    x.append(7)

except AttributeError as e:
    print("Attribute Error", e)