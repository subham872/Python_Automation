name = "batman"
print(len(name))

# strings are stored in  python
# Index start from 0
# len start from 1

print(name[0])

print(name[5])
# print(name[6]) #IndexError: string index out of range

print(len(name) + 1)
print(name[len(name) - 3]) # so length of name=6 -3 =3 and third index of batman is m

#string are immutable
#which means if any thing is assigned it can not be changed only it will be replaced

nameA= "Subham"
print(nameA[0])

#nameA[0] = "A"  it will give TypeError: 'str' object does not support item assignment