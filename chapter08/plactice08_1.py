import random
from code08_1 import prime_test2


def mk_num(n):
    return random.randint(10 ** (n - 1), 10 ** n-1)


def fd_prime(n):
    cnt = 1
    while True:
        d = mk_num(n)
        if prime_test2(d):
            break
        cnt += 1
    return d, cnt


prime, cnt = fd_prime(3)

print(str(prime)+"を"+str(cnt)+"回目で見つけた")
