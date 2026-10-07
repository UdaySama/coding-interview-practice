def inverted_Pyramid(n):
    for i in range(n, 0, -1):
        print("  " * (n - i) + "* " * (2 * i - 1))


inverted_Pyramid(5)