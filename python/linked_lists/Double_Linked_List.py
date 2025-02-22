class DoublyNode:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Reference to the next node
        self.prev = None  # Reference to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # The head of the list

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node  # If list is empty, new node becomes head
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node
        last.next = new_node  # Link the last node to the new node
        new_node.prev = last  # Set the previous pointer of the new node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next  # Remove the head node
            if self.head:
                self.head.prev = None
            current = None
            return

        while current and current.data != data:
            current = current.next

        if current is None:  # Data not found
            print("Data not found.")
            return

        if current.next:
            current.next.prev = current.prev  # Link the previous node to the next node
        if current.prev:
            current.prev.next = current.next  # Link the next node to the previous node
        current = None

# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.display()  # Should display: 1 <-> 2 <-> 3 <-> None
    dll.delete(2)
    dll.display()  # Should display: 1 <-> 3 <-> None
