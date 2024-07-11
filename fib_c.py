# https://habr.com/ru/companies/alconost/articles/571366/

import c_module
from time import time

# Python fib version using recursion
def py_fib(n):
    if (n <= 1):
        return n
    return py_fib(n-1) + py_fib(n-2)

n = 36

# C test
t = time()
c_res = c_module.c_fib(n)
c_time = time() - t

# Python test
t = time()
py_res = py_fib(n)
py_time = time() - t

print(f'Input: {n}\n{py_res=}, {py_time=}\n{c_res=}, {c_time=}') 

# Input: 36
# py_res=14930352, py_time=3.3464136123657227
# c_res=14930352, c_time=0.03532052040100098