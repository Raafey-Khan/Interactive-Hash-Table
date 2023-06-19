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

# Usage example with user interaction:
size = int(input("Enter the size of the hash table: "))
hash_table = HashTable(size)

while True:
    print("1. Insert key-value pair")
    print("2. Search for a key")
    print("3. Delete a key")
    print("4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        hash_table.insert(key, value)
        print("Key-value pair inserted.")
    elif choice == 2:
        key = input("Enter the key to search: ")
        result = hash_table.search(key)
        if result is not None:
            print("Value:", result)
        else:
            print("Key not found.")
    elif choice == 3:
        key = input("Enter the key to delete: ")
        hash_table.delete(key)
        print("Key deleted.")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")
