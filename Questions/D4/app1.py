nums = [10,20, 30, 65,4,45, 99]

def secondLargest(arr):
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif second > num and num != first:
            second = num 
    return second

result = secondLargest(nums)
print(result)