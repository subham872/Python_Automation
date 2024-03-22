# Write a program that classifies a triangle based on its side lengths.

side1 = int(input("Enter side 1"))
side2 = int(input("Enter side2"))
side3 = int(input("Enter side 3"))

if side1 == side2 == side3:
    print("This is an equilateral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("This is an isosceles Triangle")
else:
    print("This is a scalene Triangle")

