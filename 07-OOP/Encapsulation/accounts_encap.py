class Account:
    def __init__(self, number, accounttype, balance):
        self.number = number
        self.account = accounttype
        self.balance = balance

    def setnumber(self, number):
        self.number = number

    def getnumber(self):
        return self.number

    def setaccounttype(self, accounttype):
        self.account = accounttype

    def getaccounttype(self):
        return self.account

    def setbalance(self, balance):
        self.balance = balance

    def getbalance(self):
        return self.balance
# deposit methode
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposit Amount:", amount)
        print("New Balance:", self.balance)

#withdraw methode
    def withdraw(self, amount):
        if self.balance >= amount:
           self.balance = self.balance - amount
           print('Withdraw Amount:', amount)
           print('Remaining Balance:', self.balance)
        else:
           print("Insufficient Balance")

#fund transfer
    def fund_transfer(self,other_account,amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            other_account.balance = other_account.balance + amount
            print("Transferred Amount:", amount,"to account",other_account.number)
            print("Remaining Balance A/c A:", self.balance)
            print("New Balance A/c B:", other_account.balance)
        else:
            print("Transfer Failed: insufficient Balance")

#pay bills
    def pay_bills(self, amount, bill_name):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Bill Paid:", bill_name)
            print("Amount", amount)
        else:
            print("Insufficient Balance")


a = Account(22462050, "Current", 50000)
b = Account(22462056, "Saving", 30000)
print("Account No.:", a.getnumber())
print("Account Type:", a.getaccounttype())
print("Balance:", a.getbalance())

print("\n--- Deposit ---")
a.deposit(20000)

print("\n--- Withdraw ---")
a.withdraw(10000)

print("\n---Fund Transfer ---")
a.fund_transfer(b,5000)

print("\n--- Pay_bills ---")
a.pay_bills(5000, "Electricity")

print("\nFinal Balance A/c A:", a.getbalance())
print("\nFinal Balance A/c B:", b.getbalance())