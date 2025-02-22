class Stack:
    def __init__(self):
        # Initialize the stack as an empty list
        self.stack = []

    def push(self, data):
        # Add an element to the top of the stack
        self.stack.append(data)

    def pop(self):
        # Remove and return the top element of the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty."

    def peek(self):
        # Return the top element without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty."

    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0

    def size(self):
        # Return the number of elements in the stack
        return len(self.stack)


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top element:", stack.peek())  # Output: 30
print("Stack size:", stack.size())   # Output: 3
print("Pop element:", stack.pop())   # Output: 30
print("Stack size after pop:", stack.size())  # Output: 2
