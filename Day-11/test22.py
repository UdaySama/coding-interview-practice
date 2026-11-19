name = 'siddharth syyed'
rev = ""
word = ""

for char in name:
    if char == " ":
        rev = word + " " + rev
        word = ""
    else:
        word = word + char

rev = word + rev
print(rev)