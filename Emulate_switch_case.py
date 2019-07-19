#Emulating switch case statement in python
#row code basic meaning
if cond=='conda':
   functiona()
elif cond=='condb':
   functionb()
else:
   function_default()

def myfunc(a,b):
    return a+b

functs=[myfunc]
funcs[0](2,3)
#5

func_dict={
'conda':functiona,
'condb':functionb
}

#func_dict[cond]() ...does not pass default 

func_dict.get(cond,function_default)()

#example

def dispatch_if(operator,x,y):
    if operator=='add':
        return x+y
    elif operator=='sub':
        return x-y
    elif operator=='mul':
        return x*y
    elif operator=='div':
        return x/y

dispatch_if('mul',2,8)
#16
#lambda x,y: x+y-->def function (x,y): return x+y-->x=1,y=2,def function (): return x+y-->x=1,y=2,lambda:x+y

#dict.get(key,else)

def dispatch_dict(operator,x,y):
    return{
        'add': lambda: x+y,
        'sub': lambda: x-y,
        'mul': lambda: x*y,
        'div': lambda: x/y
    }.get(operator,lambda: None)()
