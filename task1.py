class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def delete(self, key):
        index = self.hash_function(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return
        raise KeyError("Key not found in the table")

# Екземпляр таблиці хешу
hash_table = HashTable()

# Додаємо декілька елементів у таблицю хешу
hash_table.insert(10, "A")
hash_table.insert(20, "B")
hash_table.insert(30, "C")
hash_table.insert(25, "D")

# Виводимо вміст таблиці хешу до видалення
print("До видалення:", hash_table.table)

# Видаляємо елемент з ключем 20
hash_table.delete(20)

# Виводимо вміст таблиці хешу після видалення
print("Після видалення:", hash_table.table)
