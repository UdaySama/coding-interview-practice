def missingNUm(arr,n):
    excepted_Sum = n * (n + 1) // 2
    return excepted_Sum - sum(arr)

print(missingNUm([1,2,3,5],5))