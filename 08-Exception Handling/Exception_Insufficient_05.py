class InsufficientFundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, balance):
        self.balance = balance
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 15000:
            raise InsufficientFundException("You can not deposit more than 15000 in a single transaction.")
        self.balance += amount
        print(f"(Deposited {amount}, Current Balance {self.balance})")

    def withdraw(self, amount):
        if amount > 6000:
            raise InsufficientFundException("You can not withdraw more than 6000 in a single transaction.")
        if self.count >= 3:
            raise InsufficientFundException("Withdrawal limit exceeded, You can not withdraw more than 3 times.")
        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"(Withdrawn {amount}, Current Balance {self.balance})")

        else:
            raise InsufficientFundException("Insufficient funds, minimum 2000 must be remain in the account.")

acc=Account()
acc.set_balance(10000)

try:
    acc.deposit(12000)
    acc.deposit(16000)
    acc.withdraw(5500)
    acc.withdraw(6000)
    acc.withdraw(6000)
    acc.withdraw(6000)

except Exception as e:
    print("Error occurred:", e)

print("Hello world")