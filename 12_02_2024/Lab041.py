# Write a program that classifies a triangle based on its side lengths.
side1 = float(input("Enter first number\n"))
side2 = float(input("Enter second number\n"))
side3 = float(input("Enter third number\n"))

if side1 == side2 == side3:
    print("This is an equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("This is an isosceles triangle")
else:
    print("This is a scalene triangle")


# break

for i in range(1, 8):
    if i == 6:
        break
    print(i)
print("outside the loop")

for i in range(0, 8):
    if i == 6:
        break
    print(i)
print("outside the loop")

for counter in range(0, 11):
    print(counter)
    if counter == 5:
        break
print("outside counter")
