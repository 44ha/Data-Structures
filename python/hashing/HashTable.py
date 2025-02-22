class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a fixed size
        self.size = size
        self.table = [[] for _ in range(size)]  # Each index will have a list to store key-value pairs

    def _hash(self, key):
        # A simple hash function that maps the key to an index
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert key-value pair into the hash table
        index = self._hash(key)
        
        # Check if the key already exists and update it
        for idx, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][idx] = (key, value)  # Update value if key exists
                return
        
        # If key does not exist, append the new pair
        self.table[index].append((key, value))

    def get(self, key):
        # Retrieve value for the given key
        index = self._hash(key)
        
        # Search for the key in the corresponding list (chain)
        for k, v in self.table[index]:
            if k == key:
                return v
        
        # Return None if key is not found
        return None

    def delete(self, key):
        # Delete the key-value pair
        index = self._hash(key)
        
        # Search and remove the key-value pair
        for idx, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][idx]  # Remove the pair
                return True
        
        # Return False if key is not found
        return False

    def display(self):
        # Display the contents of the hash table
        for index, chain in enumerate(self.table):
            if chain:
                print(f"Index {index}: {chain}")

# Example usage
hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("name", "Alice")
hash_table.insert("age", 25)
hash_table.insert("city", "New York")

# Display the hash table
print("Hash Table Contents:")
hash_table.display()

# Retrieve a value
print("\nGet 'name':", hash_table.get("name"))  # Output: Alice
print("Get 'age':", hash_table.get("age"))    # Output: 25
print("Get 'city':", hash_table.get("city"))  # Output: New York

# Delete a key-value pair
print("\nDelete 'age':", hash_table.delete("age"))  # Output: True
print("Delete 'country':", hash_table.delete("country"))  # Output: False

# Display the hash table after deletion
print("\nHash Table Contents After Deletion:")
hash_table.display()
