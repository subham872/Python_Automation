# Encapsulation
class HDFC:
    def __init__(self, ac_number, balance):
        self.ac_number = ac_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
        else:
            print("Insufficient funds")
    def available(self):
        return self.__balance
cash=HDFC(13747,1000)
cash.deposit(500)
cash.withdraw(100)
print("My available balance is ",cash.available())

