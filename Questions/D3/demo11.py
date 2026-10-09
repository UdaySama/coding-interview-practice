def countCharFreq(str):
    freq={}
    for char in str:
        freq[char]=freq.get(char,0) + 1

    return freq


print(countCharFreq("machine test"))