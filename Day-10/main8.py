def find_Largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = [10, 5, 8, 20, 3]
largestNum =find_Largest(nums)
print(largestNum)
