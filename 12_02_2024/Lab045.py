# Factorial
# n = 5
# it means 5!= 5*4*3*2*1=120

num = int(input("Enter the number\n"))
if num < 0:
    print("Factorial is not defined for negative numbers")
elif num == 0:
    print("factorial of o is 1")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
print("Factorial of",num, "is" ,fact)

