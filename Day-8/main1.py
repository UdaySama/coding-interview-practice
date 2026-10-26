list = [1, 2]
try:
    list('ab')
except TypeError as e:
    print(type(e).__name__)