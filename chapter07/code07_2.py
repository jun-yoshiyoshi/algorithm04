class Knapsack:

    def __init__(self, size):
        self.size = size
        self.weight = 0
        self.value = 0
        self.items = []

    def append(self, item):
        if not self.has_room_for(item):
            raise ValueError("重量オーバーです。")
        self.items.append(item)
        self.weight += item.weight
        self.value += item.price

    def has_room_for(self, item):
        return self.size >= self.weight + item.weight

    def __str__(self):
        val = f"重量{self.weight}kg　/　価値{self.value}万円"
        return val
