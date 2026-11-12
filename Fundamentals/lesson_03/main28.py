arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even = []
odd = []

for num in arr:
    if num % 2 == 0:
        even.append(num * 2)
    else:
        odd.append(num * 2)

print(even)
print(odd)