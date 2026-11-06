arr = [1, 2, 3, 5]
n = 5
x1 = 0
for i in range(1, n + 1):
    x1 ^= i
x2 = 0
for num in arr:
    x2 ^= num

print(x1 ^ x2)