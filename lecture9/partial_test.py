def f(x):
    return 2*x

print(f(10))

from functools import partial
g = partial(f, 15)

print(g())
print("--------")
def add(x, y):
    return x + y 

only_one = partial(add, 10)
no_arg = partial(only_one, 20)

print("No arg: ", no_arg())
print("Only one: ", only_one(25))
print("Add: ", add(50, 20))
