nums = [1, 3, 2, 3, 4, 1, 5]

unique = [] 

[unique.append(x) for x in nums if x not in unique]

print(unique)