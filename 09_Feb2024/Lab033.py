a = 46
b = 45
x = 10
y = 67

result1 = (a > b)
result2 = (x < y)
result3 = result1 and result2
print(result3)

value1 = 20
value2 = 30
value3 = 40
# value 1 is greater than value2 and value3
# value 2 is greater than value1 and value3
# value 3 is greater than value 1 and value2
if value1 > value2 and value1 > value3:
    print("Value 1 is maximum")
elif value2 > value1 and value2 > value3:
    print("Value 2 is maximum")
else:
    print("Value3 is maximum")
