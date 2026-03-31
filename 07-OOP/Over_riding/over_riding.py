class Bank:
    def get_interest(self):
        print("Interest is:", 5)

class Sbi(Bank):
    def get_interest(self):
        print("Interest is:", 7)

class Hdfc(Bank):
    def get_interest(self):
        print("Interest is:", 6)

class Icici(Bank):
    def get_interest(self):
        print("Interest is:", 6.5)


b=Bank()
s=Sbi()
h=Hdfc()
i=Icici()

b.get_interest()
s.get_interest()
h.get_interest()
i.get_interest()

# class Bikes:
#     def get_model(self):
#         print("Print bike models are:", 8)
#
# class Hero(Bikes):
#     def get_model(self):
#         print("Print bike model is:", 2)
#
# class Honda(Bikes):
#     def get_model(self):
#         print("Print bike model is:", 3)
#
# class Bajaj(Bikes):
#     def get_model(self):
#         print("Print bike model is:", 5)
#
# a=Bikes()
# b=Hero()
# c=Honda()
# d=Bajaj()
#
# a.get_model()
# b.get_model()
# c.get_model()
# d.get_model()
#
# class Zameen:
#     def get_zameen(self):
#         print("Zameen bahut tarah ki hoti hai")
#
# class Acre(Zameen):
#     def get_zameen(self):
#         print("Zameen acre me hai:", 20)
#
# class Beega(Zameen):
#     def get_zameen(self):
#         print("Zameen beega me hai:", 40)
#
# class Hectare(Zameen):
#     def get_zameen(self):
#         print("Zameen hectare me hai:", 10)
#
# a=Zameen()
# b=Acre()
# c=Beega()
# d=Hectare()
#
# a.get_zameen()
# b.get_zameen()
# c.get_zameen()
# d.get_zameen()
