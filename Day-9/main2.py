def two_sum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i


print(two_sum([9,7,5,2],12))