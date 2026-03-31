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
        print(f"Deposited {amount}, Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > 4000:
            raise InsufficientFundException("You can not withdraw more than 4000 in a single transaction")

        if self.count >= 4:
            raise InsufficientFundException("Withdrawal limit exceeded, you can not withdraw more than 4 times")

        if self.balance -amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"Withdrawn {amount}, Remaining Balance: {self.balance}")

        else:
            raise InsufficientFundException("Insufficient funds, minimum 2000 must be remain in account")

acc=Account()
acc.set_balance(5000)

try:
    acc.deposit(5000)
    acc.withdraw(3900)
    acc.withdraw(3000)
    acc.withdraw(2000)
except InsufficientFundException as e:
    print("Exception occurred:", e)
