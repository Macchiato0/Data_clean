scores = {'Loi': 95, 'Bui': 78, 'Dea': 82}
#key:value 
print(scores['Loi'])
print(scores['Dea'])
# loop through dictionary(i.e. loop keys and get value through key)
# %s:string, %d:digit,\t:tab
for elem in scores:
    print('%s\t--->\t%d' % (elem, scores[elem]))

# updates value of a key
scores['Bui'] = 65

#add an element of a dictionary    
scores['Zolo'] = 71
scores.update(Nono=67, Hido=85) #keyword can't be an expression. i.e. no quotes to define key as strings in update()
print(scores)
    
if 'Witi' in scores:
    print(scores['Witi']) #no error alert

print(scores.get('Witi')) #None

# get() could set a default parameter

print(scores.get('Witi', 60))

# delete an element
# popitem() i.e. delete the first element
print(scores.popitem())

#pop() i.e. delete a specific element
print(scores.pop('Loi',95))

# clean the dictionary
scores.clear()
print(scores)

#zip 2 lists to dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
