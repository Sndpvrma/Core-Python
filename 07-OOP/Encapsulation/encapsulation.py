class Account:
    def __init__(self):
        self.__number = 0
        self.__account_type = 0
        self.__balance = 0

    def set_number(self, number):
        self.__number = number

    def get_number(self):
        return self.__number

    def set_account_type(self, account_type):
        self.__account_type = account_type

    def get_account_type(self):
        return self.__account_type

    def set_balance(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

a = Account()
a.set_number("12345")
a.set_account_type("Saving")
a.set_balance("5000")

print("Account Number", a.get_number())
print("Account Type", a.get_account_type())
print("Account Balance", a.get_balance())