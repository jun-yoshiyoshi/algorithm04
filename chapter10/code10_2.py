from code10_1 import bsorted_str


def block_sort_decode(val, idx):
    char_last_idx = []
    for i, v in enumerate(val):
        char_last_idx.append((v, i))

    char_last_idx.sort()

    last_to_front_idx = [0] * len(char_last_idx)
    for i, v in enumerate(char_last_idx):
        last_to_front_idx[v[1]] = i
    res = val[idx]

    i = last_to_front_idx[idx]
    while i != idx:
        res += val[i]
        i = last_to_front_idx[i]
    return res[::-1]


print(block_sort_decode(*bsorted_str))
