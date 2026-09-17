def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

def first_non_repeating(s):
    freq = char_frequency(s)
    for c in s:
        if freq[c] == 1:
            return c
    return None