# Exceception handling

# Try and except block
# try the code
# execute except code if problem

a = int(input("Enter number one\n"))
b = int(input("Enter number two\n"))

try:
    c=a/b
    print("Div is",c)
except ZeroDivisionError:
    print("Divison by zero is not allowed")
except ValueError:
    print("Please use integer")