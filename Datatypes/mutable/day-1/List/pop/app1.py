def remove_last(lst):
    lst = lst.copy()
    popped = lst.pop()
    return popped, lst


print(remove_last([1,2,3,4,5]))