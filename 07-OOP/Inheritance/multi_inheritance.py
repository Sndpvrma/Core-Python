# class Addition:
#     def sum(self, a, b):
#         return a+b
#
# class Multiplication:
#     def multiply(self, a, b):
#         return a * b
#
# class Derived(Addition, Multiplication):
#     def divide(self, a, b):
#         return a/b
#
# derived_obj = Derived ()
# print(derived_obj.sum(60,30))
# print(derived_obj.multiply(60,30))
# print(derived_obj.divide(60,30))

class Addition:
    def sum(self, a, b):
        return a + b

class Multiplication:
    def multiply(self, a, b):
        return a * b
class Derived(Addition, Multiplication):
    def divide(self, a, b):
        return a / b

derived_obj = Derived()
print(derived_obj.multiply(90,-10))
print(derived_obj.divide(90,45))
print(derived_obj.sum(90,70))
