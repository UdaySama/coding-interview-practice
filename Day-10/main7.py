def count_Frequency(numbers):
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num]+=1
        else:
            frequency[num]=1
    return frequency


nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
frequency_Count = count_Frequency(nums)
print(frequency_Count)