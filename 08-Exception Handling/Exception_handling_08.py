# from itertools import count

class InsufficientFundsException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def setbalance(self, balance):
        self.balance = balance
    def getbalance(self):
        return self.balance

    def deposite(self, amount):
        self.balance += amount
        print(f"Deposite: {amount}, current balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 20000:
            raise InsufficientFundsException('You can not withdraw more than 2000 in a single transaction')
        if self.count >= 2:
            raise InsufficientFundsException('Withdraw limit exceeded. Maximum 3 withdrawal allowed.')

        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"Withdraw: {amount}, Remaining balance: {self.balance}")

        else:
            raise InsufficientFundsException('Insufficient balance. Minimum 2000 must remain in the account.')

acc=Account()
acc.setbalance(50000)

try:
    acc.deposite(2000)
    acc.withdraw(3000)
    acc.withdraw(2500)

except InsufficientFundsException as e:
    print('Exception:', e)
