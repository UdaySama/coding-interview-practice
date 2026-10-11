from  functools import reduce

numbers = [1, 2, 3, 4]

print(list(filter(lambda x: x%2 == 0, numbers)))