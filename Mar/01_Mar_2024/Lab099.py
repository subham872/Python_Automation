# class MyCustomException(Exception):
#
#     def __init__(self,message):
#         self.message=message


balance = 100
withdraw_amount = int(input("Enter the amount you can withdraw\n"))

if withdraw_amount > balance:
    print("Balance is low")
else:
    print("Total after withdraw", balance - withdraw_amount)
