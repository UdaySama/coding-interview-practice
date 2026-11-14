from functools import cmp_to_key

def cmp(a,b):
    return(a>b)-(a<b)

print(sorted([1,5,2,8,9,4],key=cmp_to_key(cmp)))