l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
common = []
for num in l1:
    if num in l2:
        common.append(num)

print(common)