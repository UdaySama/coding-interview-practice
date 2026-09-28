def toUpperCase(str):
    res = []
    for char in str:
        if 'a' <= char <= 'z':
            res.append(chr(ord(char) - 32))
        else:
            res.append(char)
    return "".join(res)


print(toUpperCase("hello"))
print(toUpperCase("UdaYsInK"))

