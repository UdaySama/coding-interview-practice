def namual_revs(lst):
    reversed_List =[]
    for i in range(len(lst) -1 , -1, -1):
        reversed_List.append(lst[i])
    return reversed_List

print(namual_revs([1,2,3]))