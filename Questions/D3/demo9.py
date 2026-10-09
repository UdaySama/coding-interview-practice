import re

def isPalindrome_(str):
    cleaned = re.sub(r'[^a-zA-Z0-9]', '',str).lower()
    return cleaned == cleaned[::-1]


print(isPalindrome_("A man, a plan, a canal: Panama"))
