def add_range(lst,st,end):
    lst.extend(range(st,end))
    return lst

print(add_range([0],1,5))
