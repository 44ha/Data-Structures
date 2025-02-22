class DynamicArray:
    def __init__(self):
        # Start with an empty array and a small size.
        self.array = [None] * 1  # Initialize array with 1 space
        self.capacity = 1  # The array starts with one space
        self.size = 0

    def insert(self, value):
        # Add a value to the array. If it's full, make more space.
        if self.size == self.capacity:
            self._resize()  # Make the array bigger when full
        self.array[self.size] = value  # Add the value to the next available space
        self.size += 1

    def _resize(self):
        # Make the array bigger when it is full.
        self.capacity *= 2  # Double the size
        new_array = [None] * self.capacity  # Create a new bigger array
        for i in range(self.size):
            new_array[i] = self.array[i]  # Copy old values to the new array
        self.array = new_array  # Use the new bigger array

    def traverse(self):
        # Show all the values in the array.
        return [element for element in self.array if element is not None]  

# Example :
if __name__ == "__main__":
    dyn_array = DynamicArray()
    dyn_array.insert(10)  # Add 10
    dyn_array.insert(20)  # Add 20
    dyn_array.insert(30)  # Add 30
    print("The dynamic array contains:", dyn_array.traverse())  # Should show [10, 20, 30]
