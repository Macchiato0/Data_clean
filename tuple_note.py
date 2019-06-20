# define a tuple
t = ('Joe',90 , True, 'Lansing')
print(t)
# print element in a tuple, same with list
print(t[0])
print(t[3])
# loop the element of a tuple
for member in t:
    print(member)
# giving new value to an element in tuple is not allowed (immutable) 
# t[0] = 'wong'  # TypeError
# redefine a whole tuple, the previous value will be lost 
t = ('wong', 90, True, 'Lansing')
print(t)
# convert tuple to list
person = list(t)
print(person)
# element in a list is mutable
person[0] = 'Lee'
person[1] = 102
print(person)
# convert list to tuple
fruits_list = ['apple', 'banana', 'orange']
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
#tuple is the preferrable data structure for multiuser system. tuple is smaller and more stable than list
