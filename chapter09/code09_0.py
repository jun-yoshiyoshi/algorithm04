

# print("a\ta%3")
# for a in range(10):
#     print(f"{a}\t{a%3}")

# m = 3
# tmpl = "{:>3}" * 5
# スペースを挟んで右詰にする

# print(tmpl.format("a", 1, 2, 3, 4))
# for i in range(m):
#     print(tmpl.format(i, i % m, i**2 % m, i**33 % m, i**4 % m))


def make_table(m):
    tmpl = "{:>5}" * (m + 2)
    header = ["a"]
    for i in range(1, m + 2):
        header.append(i)
    print(tmpl.format(*header))
    for a in range(m):
        vals = [a]
        for i in range(1, m + 2):
            vals.append(a ** 2 % m)
        print(tmpl.format(*vals))


print("make_table(5)")
make_table(5)
print("make_table(7)")
make_table(7)
print("make_table(11)")
make_table(11)
