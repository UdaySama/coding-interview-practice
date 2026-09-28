def count_Vowels(s):
    s_lower = s.lower()
    return sum(s_lower.count(v) for v in 'aeiou')


print(count_Vowels("UdaysinhSiddharthAmeyAman"))