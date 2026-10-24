print('1. Create dict from input')

n = int(input('Entre number of pairs:- '))

d = {}
for i in range(n):
    k = input('Entre key:- ')
    v = input('Entre Value:- ')
    d[k] = v

print(d)