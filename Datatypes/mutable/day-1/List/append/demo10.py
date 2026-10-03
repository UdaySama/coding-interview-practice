def positive_ext(nums):
    positive = []
    for n in nums:
        if n > 0:
            positive.append(n)
    return positive


print(positive_ext([-5, 3, -1, 10, 0, 7]))