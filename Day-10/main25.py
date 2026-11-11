nums = [1, 2, 4, 5]
n = 5

total = n * (n + 1) // 2
missing = total - sum(nums)
print(missing)