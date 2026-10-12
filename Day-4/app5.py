r =int(input("Entre Number:- "))
for i in range(1,r+1):
    sp = "  " * (r - i)
    st = " *" * (2 * i -1)
    print(sp + st)