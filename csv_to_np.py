import csv to python
import numpy as np 
''
f=r'K:\GISElec_BusinessSupport\YiFan\Duplicate_sp\duplicate_sp.csv'
d=','
n=42
input are file, delimiter, and column number
''
#function to convert sp table to numpy array
def csv_to_np(file,delim,n_col)
    with open(file, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter="{}".format(delim))
        ary_list=[]
        for row in spamreader:
            ary=np.array(row) if len(row) = n_col else None
            ary_list.append(ary)
    return np.array(ary_list)
