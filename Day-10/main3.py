def findSecondLargest(numbers):
    largest = float('-inf')
    secondLargest = float('-inf')
    for num in numbers:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest:
             secondLargest = num
    return secondLargest


nums = [10, 5, 8, 20, 3]
find_Second_Largest=findSecondLargest(nums)
print(find_Second_Largest)
