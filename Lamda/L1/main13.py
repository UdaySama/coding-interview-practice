numbers = [1, 2, 3, 4]
nestedResult = list(map(lambda x: (lambda y : y + 10)(x), numbers))
print(nestedResult)