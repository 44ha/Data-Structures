class CircularNode:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Reference to the next node

class CircularLinkedList:
    def __init__(self):
        self.head = None  # The head of the list

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node  # If the list is empty, new node becomes head
            new_node.next = self.head  # Point the new node to itself (circular reference)
            return
        last = self.head
        while last.next != self.head:  # Traverse until we reach the head again
            last = last.next
        last.next = new_node  # Link the last node to the new node
        new_node.next = self.head  # Complete the circular reference

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # If we've cycled back to the head, stop
                break
        print("(circular)")

    def delete(self, data):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        prev = None
        while True:
            if current.data == data:
                if prev:
                    prev.next = current.next  # Bypass the current node
                else:  # If the node to delete is the head
                    if current.next == self.head:  # Only one node in the list
                        self.head = None
                    else:
                        self.head = current.next
                        last = self.head
                        while last.next != current:
                            last = last.next
                        last.next = self.head  # Fix circular link
                current = None
                return
            prev = current
            current = current.next
            if current == self.head:  # If we've cycled back to the head, stop
                break
        print("Data not found.")

# Example usage:
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)
    cll.display()  # Should display: 1 -> 2 -> 3 -> (circular)
    cll.delete(2)
    cll.display()  # Should display: 1 -> 3 -> (circular)
