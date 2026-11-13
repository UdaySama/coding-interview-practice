def fibonnaci(num):
    a, b = 0, 1
    result = []
    while a <= num:
        result.append(a)
        a, b = b, a + b
    return result

print(fibonnaci(7))