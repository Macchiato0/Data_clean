#loop the index
for i in range(len(sequence)):
    print(sequence[i])



#loop the item
for item in sequence:
    print(item)
    
    
 #loop both the item and index
for i,item in enumerate(sequence):
    print("{} : {}".format(i,item)
    
#enumerate create a tuple (index, item) of the loop
for i in enumerate(sequence): 
    print i
'''
(0, 1)
(1, 4)
(2, 2)
(3, 5)
(4, 7)
'''
