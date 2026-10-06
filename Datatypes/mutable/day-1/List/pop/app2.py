def remove_at_index(lst, idx):
    lst = lst.copy()
    return lst.pop(idx), lst


print(remove_at_index([10,20,30,40],1))