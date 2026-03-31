# Example of Polymorphism  with one Name Multiple Forms

class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is primary language of India")

    def type(self):
        print("India is developing country")

class USA():
    def capital(self):
        print("Washington DC is the capital of USA")

    def language(self):
        print("English is primary language of USA")

    def type(self):
        print("USA is developed country")

obj_ind=India()
obj_usa=USA()

for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()