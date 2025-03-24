# TASK-1 PRACTICE SET METHODS

new_set = set()
new_set.add(4) # add method
new_set.add(7)
print(new_set)

new_set.remove(7) # remove method
print(new_set)

new_set1= new_set.copy() #copy method
print(new_set1)

print(new_set.clear()) #clear method

new_set1.add(9)
new_set1.add(6)

print(new_set.union(new_set1))

set2 = frozenset(["apple", "banana","cherry"])
set3 = frozenset(["apple", "kiwi", "mango"])
print(set3.difference(set2))


# TASK-2 RESEARCH WHETHER THESE 3 METHODS FROM FRONZEN SET WORKS ON SET

#working 

a = {1,2,3,4,5,6,7,8,9}
b = {2,3}

a.discard(7)
print(a)

print(a.isdisjoint(b))

print(b.issubset(a))

print(a.issuperset(b))

