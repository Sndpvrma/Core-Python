# try:
#     import fast_math
#
# except ModuleNotFoundError:
#     print("Please install the fast_math module")
#
# except ImportError as e:
#     print("Module not found", e)

try:
    import mango_karela

except ModuleNotFoundError as e:
    print("Please import module", e)

except ImportError as e:
    print("ImportError", e)



