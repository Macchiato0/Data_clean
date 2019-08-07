#map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

Most of the times we use lambdas with map. Instead of a list of inputs we can even have a list of functions.
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]



#filter creates a list of elements for which a function returns true. 

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]


#Reduce applies a rolling computation to sequential pairs of values in a list.

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24

#Reference:
#https://book.pythontips.com/en/latest/map_filter.html
