def is_palindrome(str):
    clean = str.lower()
    return clean == clean[::-1]

print(is_palindrome('Madam'))