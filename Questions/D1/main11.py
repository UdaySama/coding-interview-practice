def count_vowels_and_consonants(s):
    vowels = "aeiou"
    v_count, c_count = 0, 0
    for char in s.lower():
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return {"vowels": v_count, "consonants": c_count}