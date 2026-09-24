n = 5 
a, b = 0, 1

fib_ser = []

for _ in range(n):
    fib_ser.append(a)
    a, b = b, a + b

print(fib_ser)