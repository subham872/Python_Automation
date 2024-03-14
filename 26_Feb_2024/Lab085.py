# Some more example of encapsulation
# security
# You can access your variables only through function and if it is private function then only you will be able to access
class ICICI:
    def __init__(self, ac_num, balance):
        self.ac_num = ac_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit Successfull,Available balance", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdraw Successfull,Available balance", self.balance)
        else:
            print("Insufficient funds")

    def available(self):
        return self.balance


cash = ICICI(11223, 1900)
cash.deposit(600)
cash.withdraw(250)
print("my available balance is", cash.available())
