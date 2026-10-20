def second_largest(lst):
    unique_Lst = list(set(lst))
    unique_Lst.sort()
    return unique_Lst[-2] if len(unique_Lst) >= 2 else None


print(second_largest([12, 45, 2, 41, 89, 89]))