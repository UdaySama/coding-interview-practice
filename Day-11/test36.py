def moveZero(arr):
    nonZeros = [x for x in arr if x != 0]
    zeors  = [0] * (len(arr) - len(nonZeros))
    return nonZeros + zeors

print(moveZero([0, 1, 0, 3, 12]))