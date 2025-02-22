class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def hash(self, key):
        """Simple hash function to calculate the index."""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair into the hash table."""
        index = self.hash(key)
        original_index = index
        
        # Handle collision by linear probing
        while self.table[index] is not None:
            if self.table[index][0] == key:  # Key already exists, update value
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size  # Move to the next slot
            if index == original_index:  # Table is full
                return "Error: Hash table is full"
        
        # Insert the key-value pair at the found index
        self.table[index] = (key, value)
    
    def get(self, key):
        """Get the value associated with the key."""
        index = self.hash(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == original_index:  # We have looped through the table
                return "Error: Key not found"
        
        return "Error: Key not found"
    
    def delete(self, key):
        """Delete the key-value pair from the hash table."""
        index = self.hash(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return "Key deleted"
            index = (index + 1) % self.size
            if index == original_index:  # We have looped through the table
                return "Error: Key not found"
        
        return "Error: Key not found"
    
    def display(self):
        """Display the current hash table."""
        for index, element in enumerate(self.table):
            if element is not None:
                print(f"Index {index}: {element[0]} -> {element[1]}")
            else:
                print(f"Index {index}: None")

# Example usage:
if __name__ == "__main__":
    hash_table = OpenAddressingHashTable(5)
    
    # Insert some key-value pairs
    hash_table.insert("name", "John")
    hash_table.insert("age", 30)
    hash_table.insert("city", "New York")
    
    # Display the table
    print("Hash table after insertions:")
    hash_table.display()
    
    # Get a value
    print("\nGet 'name':", hash_table.get("name"))
    
    # Delete a value
    print("\nDelete 'age':", hash_table.delete("age"))
    
    # Display the table after deletion
    print("\nHash table after deletion:")
    hash_table.display()
