# IOError (Input/Output Error) tab aata hai jab kisi
# file ya network ke saath koi Input/Output operation
# (jaise file kholna, read karna, ya write karna) fail ho jata hai.
# Python 3 mein, zyadaatar IOError ab OSError ke andar aate hain, lekin kaam wahi hai.

# try:
#     with open("data.txt", "r") as f:
#         print(f.read())
#
# except IOError as e:
#     print("I/O error", e)

try:
    with open("cricket.txt", "r") as f:
        print(f.read())

except IOError as e:
    print("I/O Error", e)