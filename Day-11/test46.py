from array import array
arr = array('i', [1, 2, 3, 4])
print(arr)

a = [1, 'hello', 3.14, [1, 2, 3]]
nums = []
for num in a:
    if isinstance(num,(int)):
        nums.append(num)
print(nums)