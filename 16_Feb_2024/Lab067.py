import math


def cube_list(num):
    return math.cbrt(num)


my_list = [9, 5, 6, 49, 16]
result = list(map(cube_list, my_list))

print(result)