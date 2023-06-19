class HashTable:


    def __init__(self, size):

        self.size = size

        self.table = [[] for _ in range(size)]



    def _hash_function(self, key):

        return hash(key) % self.size
    

    def insert(self, key, value):

        index = self._hash_function(key)


        self.table[index].append((key, value))


    def search(self, key):

        index = self._hash_function(key)

        for pair in self.table[index]:

            if pair[0] == key:
                return pair[1]
            

        return None
    

    def delete(self, key):

        index = self._hash_function(key)

        for i, pair in enumerate(self.table[index]):

            if pair[0] == key:
                del self.table[index][i]


                return
            



# Usage Example:


hash_table = HashTable(10)

hash_table.insert('apple', 5)

hash_table.insert('banana', 8)


hash_table.insert('orange', 3)


print(hash_table.search('banana')) # Output: 8


hash_table.delete('banana')


print(hash_table.search('banana'))