nums = [10,20, 30, 65,4,45, 99]

def secondLargest(arr):
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)
    return unique_arr[1] if len(unique_arr)>1 else None

result = secondLargest(nums)
print(result)
