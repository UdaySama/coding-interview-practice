def is_Digit(str):
    if not str:
        return False
    for char in str:
        if char < '0' or char > '9':
            return False
    return True



print(is_Digit("12345"))



