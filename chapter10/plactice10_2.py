p = 13029484142325529160278057675859771418199793915415887667143262604822998091867456519520695610374545430551058468053152467257405794784202459324043791117505269283282033102238957121905893454537518737843627
# こちらを使っても良い。p = 2**521 - 1
q = 88301801407902026726739202138197965620005436413133983858109294983959431890532621456825116199688536186064925748393033767927900577431907264510871051225548778689126932900125905788253448444634254212249591
# q = 2**607 -1
n = p * q

r = 6553


def find_s(phi_pq, r):
    k = 1
    while True:
        y = 1 + k * phi_pq
        s, d = divmod(y, r)
        if d == 0:
            return k, s
        k += 1


k, s = find_s((p-1)*(q-1), r)

public_key = r
private_key = s

top_secret = 'とんでもない秘密'

int(top_secret.encode('UTF-8').hex(), 16)

#　機密情報を整数に変換する
top_secret_int = int(top_secret.encode('UTF-8').hex(), 16)
top_secret_int

# 暗号化する。
crypto_data = pow(top_secret_int, public_key, n)
crypto_data

# 送られて来た暗号を復号化する
received_data = pow(crypto_data, private_key, n)

received_data

# 整数値をもとの文字列に戻す
bytes.fromhex(format(received_data, 'x')).decode('UTF-8')
