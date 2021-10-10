def block_sort_encode(val):
    res = []
    res.append(val)
    for i in range(len(val) - 1):
        temp = res[-1]
        res.append(temp[1:] + temp[0])
    res.sort()
    idx = res.index(val)
    encoded_str = [v[-1] for v in res]
    return "".join(encoded_str), idx


input_str = "明日の会合は午後が良いですが、良い天気だとお昼ご飯の後で眠くなってしまうので、午後は午後でも遅い時間が良いです"

bsorted_str = block_sort_encode(input_str)

# print(bsorted_str)
