class Queue:
    def __init__(self):
        # Initialize the queue as an empty list
        self.queue = []

    def enqueue(self, data):
        # Add an element to the end of the queue
        self.queue.append(data)

    def dequeue(self):
        # Remove and return the front element of the queue
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty."

    def front(self):
        # Return the front element without removing it
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty."

    def is_empty(self):
        # Check if the queue is empty
        return len(self.queue) == 0

    def size(self):
        # Return the number of elements in the queue
        return len(self.queue)


# Example usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Front element:", queue.front())  # Output: 10
print("Queue size:", queue.size())      # Output: 3
print("Dequeue element:", queue.dequeue())  # Output: 10
print("Queue size after dequeue:", queue.size())  # Output: 2
