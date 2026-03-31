class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, amount):
        self.balance = amount
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"(Deposited {amount}, Current Balance {self.balance})")

    def withdraw(self, amount):
        if amount > 5000:
            raise InsufficientFundException("You can not withdraw more than 5000 in a single transaction.")

        if self.count > 2:
            raise InsufficientFundException("Withdrawal limit exceeded, You can not withdraw more than 2 times.")

        if self.balance - amount >= 5000:
            self.balance -= amount
            self.count += 1
            print(f"Withdraw {amount}, Current Balance {self.balance}")

        else:
            raise InsufficientFundException("Insufficient funds, Minimum 2000 must be remain in Account.")

acc=Account()
acc.set_balance(15000)

try:
    acc.deposit(7000)
    acc.withdraw(5000)
    acc.withdraw(5000)
    acc.withdraw(5000)
    acc.withdraw(5000)

except InsufficientFundException as e:
    print("Error Occurred", e)