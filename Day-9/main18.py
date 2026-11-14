def second_largest(arr):
    unique = list(set(arr))
    if len(unique) < 2 : return None
    unique.sort()
    return unique[-2]

print(second_largest([5,1,9,9,4]))