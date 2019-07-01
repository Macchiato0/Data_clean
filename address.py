@check_street
def address_extract(t): #t is a string '........'
    match=re.search('\d\w+', t)
    text=re.split("\s", t)
    if match:
        x=match.group() #find the digit part in the string as street number
        if len(x)<6:
            position=text.index(x)    
            if position<(len(text)-2):
                street=text[position:position+4]
                return [re.sub(r'[^\w\s]','',s) for s in street]
               
    
street_kw=['RD','TR','AVE','ST','CT','DR','E','W','S','N','SE','NE','SW','NW']

"""
us street address structure

street number (1 word), street name (1-2 words), direction|surfix (1-2 words)

maximum 5 words
"""    
#decorat of address_extract(t)
#che_street can test if the last words in street list are amaong street key word
#if the last word is not adn address keyword, the full address will not include the last word 

"""
example constructor of a python decorator

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

"""


def check_street(func): #s is the list generated from address_extract
    def func_wrapper(s):
        if func(s):
            list=func(s) 
            sps=" "
            if list[-1] in street_kw:
                return sps.join(list)
            else:
                return sps.join(list[:-1])
    return func_wrapper



"""
select the address ignor case
SQL:
SELECT * FROM myTable WHERE UPPER(field) LIKE UPPER('%string2%')

cursor=arcpy.da.SearchCursor("AuditArea selection selection",["*"])

oid,comment=[],[]

for i in cursor:
    oid.append(i[0])
    comment.append(i[6])

for i in range(len(comment)):
    if address_extract(comment[i]):
        print address_extract(comment[i]),oid[i]
        

