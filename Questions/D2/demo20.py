def count_Vowels(str):
    count = 0 
    vowels = "aeiouAEIOU"
    for char in str:
        if char in vowels:
            count += 1
    return count

print(count_Vowels("UdaysinhSiddharthAmeyAman"))