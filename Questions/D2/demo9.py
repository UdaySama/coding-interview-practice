txt = "interview"

char_count = {}

for char in txt:
    char_count[char] = char_count.get(char, 0) + 1


print(char_count)