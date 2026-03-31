class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, balance):
        self.balance = balance
    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount}, Current Balance {self.balance}")

    def withdraw(self, amount):
        if amount > 3000:
            raise InsufficientFundException("You can't withdraw more than 3000 in a single transaction")

        if self.count > 3:
            raise InsufficientFundException("Withdrawal limit exceeded, you can't withdraw more than 3 times")

        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"Withdraw {amount}, Current Balance {self.balance}")

        else:
            raise InsufficientFundException("Insufficient funds, Minimum 1000 must be remain in the account")

acc=Account()
acc.set_balance(8000)

try:
    acc.deposit(5000)
    acc.withdraw(3000)
    acc.withdraw(2900)
    acc.withdraw(2500)
    acc.withdraw(2000)
    acc.withdraw(2000)

except InsufficientFundException as e:
    print("Error Occurred:", e)