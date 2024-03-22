#union with set
set1={1,2,3,4}
set2={2,3,4,5,6,7}
set3= set1.union(set2)
print(set3)

#intersection with sets
set4= {2,4,6,8,3}
set5={2,9,3,5}
set6=set4.intersection(set5)
print(set6)
#difference with sets
set4= {2,4,6,8,3}
set5={2,9,3,5}
set6=set5.difference(set4)
print(set6)

#it means from set4 remove the duplicated which are in set5
