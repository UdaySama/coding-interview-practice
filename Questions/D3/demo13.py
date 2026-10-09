def firstNonRepatingChar(str):
    freq={}
    for char in str:
        freq[char]=freq.get(char,0)+1
    for char in str:
        if freq[char]==1:
            return char
    return None

print(firstNonRepatingChar("swiss"))