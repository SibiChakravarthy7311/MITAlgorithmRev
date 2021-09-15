class HashTable(object):
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        self.n = 0

    def get_hash(self, s):
        h = 0
        for c in s:
            h += ord(c)
        return h % self.MAX

    # def add(self, key, val):
    #     key = self.get_hash(key)
    #     self.arr[key] = val
    #     self.n += 1

    # def get(self, key):
    #     key = self.get_hash(key)
    #     return self.arr[key]

    # def delete(self, key):
    #     key = self.get_hash(key)
    #     self.arr[key] = None
    #     self.n -= 1

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))
        self.n += 1

    def __getitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        # if not self.arr[h]:
        #     return
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                self.n -= 1
                break
                
    def __len__(self):
        return self.n


t = HashTable()
t["march 6"] = 310
t["march 7"] = 340
t["march 8"] = 380
t["march 17"] = 469
print(t.arr)
print(len(t))

print(t["march 6"])
print(t.arr)
del t['march 17']
del t['march 6']
print(t.arr)
print(t.n)
