class MinHeap:
    def __init__(self):
        # Initialize an empty heap
        self.heap = []

    def insert(self, value):
        # Add a new value to the heap
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        # Remove and return the smallest value (root)
        if len(self.heap) == 0:
            return "Heap is empty."
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Replace root with last element
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        # Reorganize the heap to maintain the heap property
        self._heapify_down(0)
        
        return min_value

    def peek(self):
        # Return the smallest value (root) without removing it
        if len(self.heap) == 0:
            return "Heap is empty."
        return self.heap[0]

    def _heapify_up(self, index):
        # Move the element up to maintain heap property
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                # Swap if the child is smaller than the parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        # Move the element down to maintain heap property
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index
        
        # Check if left child exists and is smaller than current
        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index
        
        # Check if right child exists and is smaller than current
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index
        
        # If the smallest value is not the current node, swap and heapify down
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def size(self):
        # Return the number of elements in the heap
        return len(self.heap)

    def is_empty(self):
        # Check if the heap is empty
        return len(self.heap) == 0


# Example usage
min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(20)
min_heap.insert(5)
min_heap.insert(1)

print("Min Heap:", min_heap.heap)        # Output: [1, 10, 5, 20]
print("Extract Min:", min_heap.extract_min())  # Output: 1
print("Min Heap after extraction:", min_heap.heap)  # Output: [5, 10, 20]
print("Peek:", min_heap.peek())  # Output: 5
