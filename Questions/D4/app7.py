def removeDupicates(lst):
    uniqueList = []
    for item in lst:
        if item not in uniqueList:
            uniqueList.append(item)

    return uniqueList

nums = [1,2,3,4,6,7,5,4,3,2,1]
result = removeDupicates(nums)
print(result)