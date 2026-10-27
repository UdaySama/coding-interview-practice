x = 1
def f():
    print(x)
    x = 2

try:
    f()
except UnboundLocalError as e:
    print(type(e).__name__)