def address_extract(t): #t is a string '........'
    match=re.search('\d\w+', t)
    text=re.split("\s", t)
    if match:
        x=match.group() #find the digit part in the string as street number
        if len(x)<6:
            position=text.index(x)    
            if position<(len(text)-2):
                street=text[position:position+3]
                return street
    

    
