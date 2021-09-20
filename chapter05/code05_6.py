class Hash_table:

    def __init__(self, size=100):
        self.data = [[] for _ in range(size)]
        self.n = size

    def get_hash(self, v):
        return hash(v) % self.n

    def search(self, key):
        i = self.get_hash(key)
        for j, v in enumerate(self.data[i]):
            if v[0] == key:
                return (i, j)
        return (i, -1)

    def set(self, key, value):
        i, j = self.search(key)
        if j != -1:
            self.data[i][j][1] = value
        else:
            self.data[i].append([key, value])

    def get(self, key):
        i, j = self.search(key)
        if j != -1:
            return self.data[i][j][1]
        raise KeyError(f"{key}was not found in this Hash_table")


# table = Hash_table()

# table.set("apple", 10)
# table.set("bluevery", 20)
# table.set("cut lemmon", 30)
# print(table.get("bluevery"))
# print(table.get("apple"))
# print(table.get("orange"))
