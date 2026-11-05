nums = [10, 20, 30, 65, 4, 45, 99]

def second_Largest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second

result = second_Largest(nums)
print(result)  