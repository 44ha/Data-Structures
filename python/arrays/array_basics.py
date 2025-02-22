# Code for basic array operations: create, add, remove

class Array:
    def __init__(self, size):
        #Create an array with a given size. It starts empty.
        self.size = size
        self.array = [None] * size  # Create an empty array

    def insert(self, index, value):
        #Put a value in the array at the given position.
        if index < 0 or index >= self.size:
            return "Error: Index is out of range!"
        self.array[index] = value

    def delete(self, index):
        #Remove the value at the given position.
        if index < 0 or index >= self.size:
            return "Error: Index is out of range!"
        self.array[index] = None  # Remove the value by setting it to None

    def traverse(self):
        #Show all the values in the array.
        return [element for element in self.array if element is not None]

# Example :
if __name__ == "__main__":
    my_array = Array(5)  # Make an array with 5 positions
    my_array.insert(0, 10)  # Add 10 at position 0
    my_array.insert(1, 20)  # Add 20 at position 1
    print("The array contains:", my_array.traverse())  # Should show [10, 20]
