def count_vowels(str):
    return sum(1 for char in str if char.lower() in 'aeiou')


print(count_vowels('ameyudaysidharthbasu'))