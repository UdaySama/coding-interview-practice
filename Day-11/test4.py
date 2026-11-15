nums = [1, 2, 3, 2, 3, 5]
freq = {x: nums.count(x) for x in set(nums)}
print(freq)