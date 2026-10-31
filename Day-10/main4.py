def bubble_Sort(elements):
    n = len(elements)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if elements[j] > elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j]


nums = [5, 2, 8, 1, 9]
bubble_Sort(nums)
print(nums)