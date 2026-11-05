def findSecondeLaregest(arr):
    uniqueNums = list(set(arr))
    print(uniqueNums)
    if len(uniqueNums) < 2 :
        return None
    uniqueNums.sort()
    return uniqueNums[-2]

print(findSecondeLaregest([1,2,3,2,1,4,5,3,2,6,8,9,0]))