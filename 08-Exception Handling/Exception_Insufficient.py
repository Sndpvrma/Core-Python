class InsufficientFundException(Exception):
    def __init__(self, msg):
        self.msg = msg
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
        print(f"Deposited:{amount}, Current Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > 2000:
            raise InsufficientFundException("You can not withdraw more than 2000 in a single transaction")

        if self.count >= 2:
            raise InsufficientFundException("Withdrawal limit exceeded. Maximum 3 withdrawals allowed.")

        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"Withdrawal:{amount}, Current Balance: {self.balance}")

        else:
            raise InsufficientFundException("Insufficient balance. Minimum 2000 must remain in the account")

acc = Account()
acc.set_balance(5000)

try:
    acc.deposit(5000)
    acc.withdraw(1500)
    acc.withdraw(1900)
    acc.withdraw(1000)

except InsufficientFundException as e:
    print("Exception raised:", e)


