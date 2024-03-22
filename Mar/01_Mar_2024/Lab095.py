try:
    a = int(input("Enter Number one\n"))
    b = int(input("Enter Number two\n"))
    c = a / b
    print("Division is", c)
except ZeroDivisionError:
    print("This is not divided by zero")
except TypeError:
    print("this is a prrint error")