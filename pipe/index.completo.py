import functools
reduce = functools.reduce

add7 = lambda x: x + 7
times10 = lambda x: x * 10
minus20 =lambda x: x - 20

pipe = lambda fns, x: reduce(lambda x, f: f(x), fns, x)

ex01 = pipe([add7, times10, minus20], 5)
print(ex01) #100

