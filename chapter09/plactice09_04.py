import random
from plactice09_3 import rabin_miller

cnt = 0
# 同じ素数を掴まないようにするため
prime_set = set()

while len(prime_set) < 10:
    n = random.randint(10**199, 10**200 - 1)
    if rabin_miller(n) == 'probably prime':
        prime_set.add(n)
    cnt += 1

print(f'{cnt}回の計算で、以下の10個を見つけた。')
for v in sorted(prime_set):
    print(v)
