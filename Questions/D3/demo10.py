def reverseSentence(str):
    words = str.strip().split()
    return " ".join(words[::-1])


print(reverseSentence("Python coding round"))