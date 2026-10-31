def remove_duplicates(numbers):
    unique_nums = []
    for num in numbers:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
remove_duplicates(nums)
print(remove_duplicates(nums))