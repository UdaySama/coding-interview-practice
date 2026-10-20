def count_vowels_consonants(s):
    vowels = 'aeiouAEIOU'
    vowels_Count = sum(1 for char in s if char in vowels)
    consonants_Count = sum(1 for char in s if char.isalpha() and char not in vowels)
    return {"vowels": vowels_Count, "consonants": consonants_Count}


print(count_vowels_consonants("Hello World"))