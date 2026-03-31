# import math
#
# try:
#     print(math.exp(1000))
#
# except ArithmeticError as e:
#     print("Calculation is too large", e)

import math

try:
    print(math.exp(1000))

except OverflowError as e:
    print("Calculation is too large", e)
