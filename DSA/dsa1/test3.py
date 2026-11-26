def reverse_Number(num):
    reversed_Num = 0 
    while num > 0:
        digit = num % 10
        reversed_Num = reversed_Num * 10 + digit
        num = num // 10
    return reversed_Num

print(reverse_Number(12345))