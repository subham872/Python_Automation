a = int(input("Enter number one\n"))

try:
    b = int(input("Enter number two\n"))
    c = a / b
    print("Div is", c)
except ValueError:
    print("Invalid input. Please enter a valid integer for the second number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except TypeError:
    print("This is a type error")
