def find_Common_Element(l1,l2):
    common_Element = []
    for item in l1:
        if item in l2:
            common_Element.append(item)
    return common_Element


lstA = [1, 2, 3, 4, 5]
lstB = [4, 5, 6, 7, 8]
common = find_Common_Element(lstA,lstB)
print(common)