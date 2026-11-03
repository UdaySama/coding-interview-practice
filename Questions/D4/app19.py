def isPalindrome(s):
    text = s.lower()
    return text == text[::-1]

print(isPalindrome('mAdam'))