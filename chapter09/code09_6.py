from code09_5 import rabin_miller


def M(n):
    return pow(2, n) - 1


for n in range(2, 1000):
    if rabin_miller(M(n)) == "probably prime":
        print("[", n, "]/", M(n))
