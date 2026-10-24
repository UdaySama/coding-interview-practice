a = 5
b = 5
print(id(a) == id(b))


print('-------------------------')

z = 10
before = id(z)
z = z + 1
print(z)

print('-------------------------')

list1 = [1,2,3]
list2 = list1.copy()
list2.append(4)
print(list1)
print(list2)

print('--------------------------')
temp = 123
del temp
# print(temp) #NameError: name 'temp' is not defined


print('--------------------------')

a, b, = 1, 2
a, b = b , a
print(a, b)