"""
range() Parameters

range([start], stop[, step])
"""

str1 = 'hello, world!'

print(len(str1))  # 13

print(str1.capitalize())  # Hello, world!

print(str1.upper())  # HELLO, WORLD!

print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1 (error)
# print(str1.index('or'))
# print(str1.index('shit'))

print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True

print(str1.endswith('!'))  # True

# 50 is the width of the print,"*"fill the vacancy,and string is placed in the center of the print
print(str1.center(50, '*'))
"""
******************hello, world!*******************
"""

# 50 is the width of the print," "fill the vacancy,and string is placed in the right end of the print
print(str1.rjust(50, ' '))
"""
                                     hello, world!
"""

str2 = 'abc123456'

#[:index of the end item] and [index of the start item:]
print(str2[2])  # c

print(str2[-1:]) #6

print(str2[:-1]) #abc12345

print(str2[2:])  # c123456

print(str2[2:5])  # c12


print(str2[2::2])  # c246 result c123456 

print(str2[::2])  # ac246 Specifying the stride of 2 as the last parameter in the Python syntax str2[::2] skips every other character
print(str2[::1])  # abc123456, last parameter=1 is the default
print(str2[::-1])  # 654321cba

print(str2[-3:-1])  # 45

print(str2.isdigit())  # False

print(str2.isalpha())  # False

print(str2.isalnum())  # True  alpha & digit

str3 = '  jackfrued@123.com '
#remove space before and after a string

print(str3.strip()) #jackfrued@123.com

