#list
#List- Collection of items, Duplicate is allowed
my_list = [1,2,3,"Subham",2]

print("Index at element 0 is",my_list[3])
my_list[3]="Anayra"
print("Index at element 3 after changing",my_list)

#append- Means in the end it will add

my_list.append(3)
print(my_list)

#append is a single item and extend is a list inside list

my_list.extend([2,"subh",4])
print(my_list)