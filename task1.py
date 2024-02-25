class HashTable:
    def __init__(self):
        self.size = 10
        self.hash_map = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def add(self, key, value):
        hash_key = self._hash_function(key)
        for i, (k, v) in enumerate(self.hash_map[hash_key]):
            if k == key:
                self.hash_map[hash_key][i] = (key, value)
                return
        self.hash_map[hash_key].append((key, value))

    def get(self, key):
        hash_key = self._hash_function(key)
        for k, v in self.hash_map[hash_key]:
            if k == key:
                return v
        raise KeyError(f"Key {key} not found")

    def delete(self, key):
        hash_key = self._hash_function(key)
        for i, (k, v) in enumerate(self.hash_map[hash_key]):
            if k == key:
                del self.hash_map[hash_key][i]
                return
        raise KeyError(f"Key {key} not found")
