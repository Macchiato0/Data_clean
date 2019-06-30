import re
def str_2_digit(s):
    if (s):
        x=re.sub("[a-zA-Z]", "",s) 
        return x


"""    
cursor=arcpy.da.SearchCursor(r"Misc Network Features\Tap Dots, T-points, & Wire Changes",["SUBSTATIONID"])
sub_list=list(set([str(i[0]) for i in cursor]))
"""    

#test if there are more than 1 x in the iterable
def test_2(x,iter):
    if iter.count(x)>1:
        return x
    else:
        False
        
cursor=arcpy.da.SearchCursor(r"Misc Network Features\Tap Dots, T-points, & Wire Changes",["SUBSTATIONID","OID@","LCP"])
"""
sub_list=['0454','1021']
"""
lcp_2=[]
for i in sub_list:
    where="SUBSTATIONID='{}'".format(i)
    cursor=arcpy.da.SearchCursor(r"Misc Network Features\Tap Dots, T-points, & Wire Changes",["SUBSTATIONID","OID@","LCP"],where)
    oid_l=[]
    lcp_l=[]
    for j in cursor:
        oid_l.append(j[1])
        lcp_l.append(j[2])
    digit_lcp=[str_2_digit(i) for i in lcp_l]
    dup_lcp=[test_2(i,digit_lcp) for i in digit_lcp]
    result=[i for i in zip(oid_l,dup_lcp) if i[1] is not None]
    lcp_2.append(result)
    
