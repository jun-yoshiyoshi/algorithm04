import random
import timeit


def mk_num(n):
    return random.randint(10**(n-1), 10**n-1)


'''
n = int(input())
print(mk_number(n))
'''


def ct_div(n, m):
    if m > n:
        n, m = m, n
    div = m
    while True:
        if n % div == 0 and m % div == 0:
            return div
        div -= 1


def ec_div(n, m):
    while True:
        r = n % m
        if r == 0:
            return m
        else:
            n, m = m, r


n, m = mk_num(10), mk_num(8)
print(ct_div(n, m), ec_div(n, m))

t1 = timeit.timeit('ct_div(n,m)', globals=globals(), number=1)

t2 = timeit.timeit('ec_div(n,m)', globals=globals(), number=1)

print(t1, t2)
