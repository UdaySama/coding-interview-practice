def runing_sum(nums):
    res= []
    total = 0
    for n in nums:
        total += n
        res.append(total)
    return res


print(runing_sum([1,2,3,4]))