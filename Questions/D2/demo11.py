import re

def is_palindrome(s: str) -> bool:
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("A man, a plan, a canal: Panama")) 
print(is_palindrome("race a car"))                     