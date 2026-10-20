def twoSum(nums, Target):
    seen = {}
    for i, num in enumerate(nums):
        diff = Target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(twoSum([2, 7, 11, 15], 9))