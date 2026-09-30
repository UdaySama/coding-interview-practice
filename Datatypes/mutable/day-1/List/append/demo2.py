def get_evens(nums):
    even= []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
    return even

print(get_evens([1, 2, 3, 4, 5]))