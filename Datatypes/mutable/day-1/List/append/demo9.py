def seprate_type(mixed):
    strings,numsbers = [], []
    for itM in mixed:
        if isinstance(itM,str):
            strings.append(itM)
        elif isinstance(itM,(int,float)):
            numsbers.append(itM)
    return strings,numsbers



print(seprate_type([1,'a',2,'b',3,'c']))
