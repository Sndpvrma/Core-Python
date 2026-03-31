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

    def Deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, Current Balance {self.balance}")

    def Withdraw(self, amount):
        if amount > 3000:
            raise InsufficientFundException("You can withdraw more than 3000 in a single transaction")

        if self.count >= 2:
            raise InsufficientFundException("Withdrawal limit exceeded, You cannot withdraw more than 3 times")

        if self.balance - amount >= 3000:
            self.balance -= amount
            self.count += 1
            print(f"Withdrawn {amount}, Current Balance {self.balance}")

        else:
            raise InsufficientFundException("Insufficient funds, minimum balance must be 2000")

acc=Account()
acc.set_balance(7000)

try:
    acc.Deposit(5000)
    acc.Withdraw(2900)
    acc.Withdraw(1000)
    acc.Withdraw(1000)
except InsufficientFundException as e:
    print("Exception occurred", e)

