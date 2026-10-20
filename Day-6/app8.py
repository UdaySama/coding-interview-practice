def second_Largest(arr):
    first = float('-inf')
    second = float('-inf')
    for num in arr:
        if num > first:
            second =first
            first = num
        elif num > second and num != first:
            second = num
    return second


print(second_Largest([1, 2, 3, 4,34, 55, 9]))
