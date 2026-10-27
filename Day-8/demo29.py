def outer():
    n = 0
    def inner():
        nonlocal n
        n += 1
    inner()
    inner()
    return n

print(outer())