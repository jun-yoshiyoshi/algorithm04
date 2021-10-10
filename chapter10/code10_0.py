import hashlib
import pickle  # 整数をバイト列に変換

# with open("python-3.7.3-embed-win32.zip", "br") as f:
#     file = f.read()

# hashlib.md5(file).hexdigest()

S = hashlib.md5("あ".encode("UTF-8")).hexdigest()

print(S)

print(hash(1))

print(hashlib.md5(pickle.dumps(1)).hexdigest())

print(hash(2))

print(hashlib.md5(pickle.dumps(2)).hexdigest())


def to_byte_hash(val):
    byte_data = pickle.dumps(val)
    return hashlib.md5(byte_data).hexdigest()


array_10k = list(range(10000))
print(to_byte_hash(array_10k))

array_10k[0] = -1
print(to_byte_hash(array_10k))
array_10k[0] = 0
print(to_byte_hash(array_10k))


def block_to_hash(block_data, nonce):
    input_str = str(block_data) + str(nonce)
    h = hashlib.sha256(input_str.encode("UTF-8")).hexdigest()

    cnt = 0
    for v in h:
        if v == "0":
            cnt += 1
        else:
            break
    return h, cnt


my_block = "prev_block_tx0_tx_1_tx_2"
c = 1
while True:
    hash_val, cnt = block_to_hash(my_block, c)
    if cnt == 3:
        print(f"{c}回目で成功しました")
        print(hash_val)
        break
    c += 1
