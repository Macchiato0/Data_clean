set1 = {1, 2, 3, 3, 3, 2}
print(set1) #set([1, 2, 3])
print('Length =', len(set1)) #('Length =', 3)
set2 = set(range(1, 10)) 
print(set2) #set([1, 2, 3, 4, 5, 6, 7, 8, 9])
set1.add(4) #add one element to set
set1.add(5) #set([1, 2, 3, 4, 5])
set2.update([11, 12]) #The A.update(B) adds elements from the set B to A.

set2.discard(5) #delete one element=5 in set2

# KeyError happens if remove() an element not in set. Do the following format to avoid error

if 4 in set2:
    set2.remove(4)
print(set2)

# loop through set
for elem in set2:
    print(elem ** 2, end=' ')
    print()

# convert tuple to set
set3 = set((1, 2, 3, 3, 2, 1))
print(set3.pop())
print(set3)

# set intersection、union、difference、symmetric_difference
print(set1 & set2)
# print(set1.intersection(set2))

print(set1 | set2)
# print(set1.union(set2))

print(set1 - set2)
# print(set1.difference(set2))
    
print(set1 ^ set2)
print(set1.symmetric_difference(set2)) #exclude intersaction
 
# test if set2 is child set of set1
print(set2 <= set1)

# test if set1 is child of set2
print(set1.issubset(set2))
print(set1 <= set2)

# test if set2 is parent set of set1
print(set2.issuperset(set1))
print(set2 >= set1)
