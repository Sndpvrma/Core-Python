# RuntimeError ek aisi category hai jisme wo errors aate hain
# jo tab trigger hote hain jab program chal toh raha hota hai,
# lekin kuch aisa ho jata hai jo kisi aur specific category
# (jaise ValueError ya TypeError) mein fit nahi baithta.
# Ise "Sabka Badla Lega" type error samajh lo—jab Python ko
# samajh nahi aata ki ise kya naam doon, toh wo use RuntimeError bol deta hai.

# 1. Recursion Depth Exceeded (Sabse Common)

# def hello():
#     return hello()
#
# try:
#     hello()
# except RuntimeError as e:
#     print("RuntimeError", e)

# 2. Dictionary Size Change (Iteration ke waqt)

# d = {'a': 1, 'b': 2, 'c': 3}
# try:
#     for key in d:
#         d.pop(key)
# except RuntimeError as e:
#     print("RuntimeError", e)

# ---------------------------------------------------------

def hello():
    return hello()
try:
    hello()
except RuntimeError as e:
    print("RuntimeError", e)


d={'a': 1, 'b': 2, 'c': 3}
try:
    for key in d:
        d.pop(key)

except RuntimeError as e:
    print("RuntimeError", e)