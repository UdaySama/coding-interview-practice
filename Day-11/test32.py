def max_Subarry(arr):
    max_so_far = arr[0]
    curr_max = arr[0]
    for num in arr[1:]:
        curr_max = max(num, curr_max + num)
        max_so_far = max(max_so_far,curr_max)
    return max_so_far

print(max_Subarry([-2, 1, -3, 4, -1, 2, 1, -5, 4]))