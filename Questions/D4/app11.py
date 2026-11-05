def removeDuplicates(lst):
    uniqueList = []
    for item in lst:
        if item not in uniqueList:
            uniqueList.append(item)
    return uniqueList

nums = [1,2,3,4,3,2,1]
result = removeDuplicates(nums)
print(result)
