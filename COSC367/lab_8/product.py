import itertools
a = [True, False]
b = [True, False]
v = (itertools.product(a, b))
for i in v:
    print(i)