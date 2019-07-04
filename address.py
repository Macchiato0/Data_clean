@check_street
def address_extract(t): #t is a string '........'
    match=re.search('\d\w+', t)
    text=re.split("[\s,,,.,?,#,/]", t)
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

cursor=arcpy.da.SearchCursor("AuditArea selection",["OID@","COMMENTS"])

oids,comments=[],[]

for i in cursor:
    oids.append(i[0])
    comments.append(i[1])

comments_oids=[]
for i in range(len(comments)):
    x=comments[i].encode('ascii', 'ignore').decode('ascii')
    t=address_extract(x)
    if t is not None:
        comments_oids.append([oids[i],t])

work_list=[]
for i in comments_oids:
    cursor=arcpy.da.SearchCursor("ELECDIST.ServiceAddress",["SERVICEPOINTOBJECTID"],"STREET like upper('%{}%')".format(i[1]))
    l=[j[0] for j in cursor]
    if len(l)==1:
        work_list.append(i[0],i[1],l[0])

[sp_oid,sp_street,polygon_oid]


work_list_distance=[]

for i in work_list:
    cursor1=arcpy.da.SearchCursor("AuditArea selection",["SHAPE@"],"OBJECTID={}".format(i[0]))
    cursor2=arcpy.da.SearchCursor(r"Customers & Transformers\Service Point",["SHAPE@"],"OBJECTID={}".format(i[2]))
    for row1 in cursor1:
        plg=row1[0]
    for row2 in cursor2:
        pt=row2[0]
    distance=plg.distanceTo(pt)
    work_list_distance.append([i,distance])
