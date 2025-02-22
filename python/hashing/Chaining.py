class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # Pointer to the next node in the chain

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash(self, key):
        """Hash function to calculate the index."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table with chaining."""
        index = self.hash(key)
        new_node = Node(key, value)
        
        # If there's no chain at the index, place the node there
        if not self.table[index]:
            self.table[index] = new_node
        else:
            # There's already a chain at this index, so we need to handle the collision
            current = self.table[index]
            while current:
                # If the key already exists, update its value
                if current.key == key:
                    current.value = value
                    return
                if not current.next:  # Find the end of the chain
                    break
                current = current.next
            # Add the new node to the end of the chain
            current.next = new_node

    def get(self, key):
        """Retrieve the value associated with a key."""
        index = self.hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value  # Return the value if the key matches
            current = current.next
        return "Error: Key not found"

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self.hash(key)
        current = self.table[index]
        prev = None
        
        while current:
            if current.key == key:
                if prev:  # If it's not the first node, remove the node by updating the link
                    prev.next = current.next
                else:  # If it's the first node, adjust the table slot
                    self.table[index] = current.next
                return "Key deleted"
            prev = current
            current = current.next
        return "Error: Key not found"

    def display(self):
        """Display the current hash table with chained nodes."""
        for index, node in enumerate(self.table):
            if node:
                print(f"Index {index}: ", end="")
                current = node
                while current:
                    print(f"({current.key}: {current.value}) -> ", end="")
                    current = current.next
                print("None")
            else:
                print(f"Index {index}: None")

# Example usage:
hash_table = HashTable()

# Insert some key-value pairs
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("country", "USA")
hash_table.insert("city", "New York")
hash_table.insert("name", "Bob")  # This will update the "name" value
hash_table.display()
# Get a value by key
print(hash_table.get("name"))  # Output: Bob
print(hash_table.get("age"))   # Output: 30

# Delete a key-value pair
print(hash_table.delete("age"))  # Output: Key deleted

# Display the hash table
hash_table.display()
