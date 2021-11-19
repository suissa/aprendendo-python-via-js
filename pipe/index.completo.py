import functools

add7 = lambda x: x + 7
times10 = lambda x: x * 10
minus20 =lambda x: x - 20

fn_pipe = lambda v, f: f(v)
ex01 = functools.reduce(fn_pipe, [add7, times10, minus20], 5)
print(ex01) #100