def is_palindrome(string):
    rev_string = string[::-1]
    return rev_string

word = "madam"

if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
