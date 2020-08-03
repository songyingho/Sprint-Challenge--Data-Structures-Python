class RingBuffer:
    def __init__(self, capacity, data=[]):
        self.index = 0
        self.capacity = capacity
        self.data = list(data)[-capacity:]

    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.index] = item
        else:
            self.data.append(item)
        
        self.index = (self.index + 1) % self.capacity

    def get(self):
        return self.data


""" in-file testing """
# buffer = RingBuffer(3)

# print(buffer.get())   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# print(buffer.get())   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# print(buffer.get())   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# print(buffer.get())   # should return ['d', 'e', 'f']
