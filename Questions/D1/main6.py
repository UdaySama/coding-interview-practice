def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq