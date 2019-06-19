fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']

for fruit in fruits:
    print(fruit.title(), end=' ')
    print()
"""
method title() returns a copy of the string in which first characters of all the words are capitalized.
"""

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)

# sorted return a list, change of list1 won't affect list2
# ['apple', 'blueberry', 'internationalization', 'orange', 'zoo']

list3 = sorted(list1, reverse=True)
# reverse specify the rule of direction

list4 = sorted(list1, key=len)
# key specify the rule of sort
 
# sort method in other fortm
list1.sort(reverse=True)
print(list1)


f = [x for x in range(1, 10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)


# list creation from iteration
# heavy consumption on cach memory
#['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 
'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']


f = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f))  #the size in kb of f 
print(f)

# generator object is created in ()
# generator does not take memory
# data is generated through calculation

f = (x ** 2 for x in range(1, 1000))
next(f)

#next(generator object) calls the next element in generator

print(sys.getsizeof(f))  #40
print(f)
for val in f:
    print(val)

