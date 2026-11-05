def removeDuplicates(lst):
    uniqueList = []
    for item  in lst:
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList


print(removeDuplicates([1,82,3,4,3,21]))