# map function
#map will take each item from the list and execute it



def squar_of_num(num):
    return num ** 2
numbers = [1, 2, 3, 4, 5]
result = list(map(squar_of_num,numbers))
print(result)
