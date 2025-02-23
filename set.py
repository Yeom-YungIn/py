#set

my_set = {1,2,3,4,5,5,5,5}
print(my_set)

my_set2 = {1,2,3}
print(my_set & my_set2)
print(my_set.intersection(my_set2))
print(my_set2.intersection(my_set))
print(my_set2.intersection(my_set2))
print('-')
print(my_set | my_set2)
print(my_set.union(my_set2))
print(my_set)

print(my_set.difference(my_set2))
print(my_set.difference_update(my_set2))
print(my_set)

