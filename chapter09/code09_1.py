
# divmod(a,b) aをｂで割った商と余りを返す。
print(divmod(2**100, 5800))

# pow(a,b,c) aのｂ乗と、aのb乗をcで割った余りを返す。
print(pow(2, 2 ** 100, 5801))

# bin(i) iの2進法の"0b+文字列"を返す
a = 43
print(bin(a))
a = a >> 4
print(bin(a))
print(int(0b101011))

print(oct(43))

print(oct(0b101011))

print(hex(43))

print(hex(0b101011))
