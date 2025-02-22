class MaxHeap:
    def __init__(self):
        # Initialize an empty heap
        self.heap = []

    def insert(self, value):
        # Add a new value to the heap
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        # Remove and return the largest value (root)
        if len(self.heap) == 0:
            return "Heap is empty."
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # Replace root with last element
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        
        # Reorganize the heap to maintain the heap property
        self._heapify_down(0)
        
        return max_value

    def peek(self):
        # Return the largest value (root) without removing it
        if len(self.heap) == 0:
            return "Heap is empty."
        return self.heap[0]

    def _heapify_up(self, index):
        # Move the element up to maintain heap property
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                # Swap if the child is greater than the parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        # Move the element down to maintain heap property
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index
        
        # Check if left child exists and is greater than current
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index
        
        # Check if right child exists and is greater than current
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index
        
        # If the largest value is not the current node, swap and heapify down
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def size(self):
        # Return the number of elements in the heap
        return len(self.heap)

    def is_empty(self):
        # Check if the heap is empty
        return len(self.heap) == 0


# Example usage
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
max_heap.insert(30)

print("Max Heap:", max_heap.heap)        # Output: [30, 20, 5, 10]
print("Extract Max:", max_heap.extract_max())  # Output: 30
print("Max Heap after extraction:", max_heap.heap)  # Output: [20, 10, 5]
print("Peek:", max_heap.peek())  # Output: 20
