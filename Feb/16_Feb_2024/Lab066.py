import math


def square_list(num):
    return math.sqrt(num)


my_list = [9, 5, 6, 49, 16]
result = list(map(square_list, my_list))

print(result)
