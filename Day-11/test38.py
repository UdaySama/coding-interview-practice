def countFreq(arr):
    freq= {}
    for item in arr:
        freq[item] = freq.get(item, 0) + 1
    return freq
print(countFreq(['a', 'b', 'a', 'c', 'b', 'a']))