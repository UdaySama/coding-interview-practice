
num = 2
is_prime = True

if num <= 1:
    is_prime = False 

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break  

if is_prime:
    print("Prime Number")
else:
    print("Not Prime Number")
    