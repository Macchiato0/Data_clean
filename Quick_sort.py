def get_pivot(ls):
    a,m,z=ls[0],ls[len(ls)//2],ls[-1]
    p=z
    if m<a:
        if m>z:
            return ls.index(m)
        elif a<z:
            return ls.index(a)
    else:
        if a>z:
            return ls.index(a)
        elif m<z:
            return ls.index(m)
    return ls.index(z)

def swap_pivot(po,ls): #po is the index of pivot, swap the pivot with the first element of a list
    ls[0],ls[po]=ls[po],ls[0]

#compare the pivot with the number to the right

def compare(bd,n_r,ls): #boarder is the index at close right side of pivot (index=0), n_r is the number go right to the end
    if ls[0]>ls[n_r]: 
       ls[bd],ls[n_r] =ls[n_r],ls[bd]
        return 1
    else:
        return 0

#run compare function on a list until the end of a list,swap pivot with the last value smaller than it (in the middle) and split the 
#list in to 2

def compare_split(ls): 
    if n_r==len(ls):
        if compare(bd,n_r,ls)==1:
            ls[0],ls[n_r]=ls[n_r],ls[0]
        else:
            ls[0],ls[bd-1]=ls[bd-1],ls[0]
    else:
        if compare(bd,n_r,ls)==1:
            bd=+1
            n_r=+1
        else:
            n_r=+1
        compare_split(ls)
        
  # keep spliting the list until there the list cannot be split 
  
  def run_split(list)
      if list
