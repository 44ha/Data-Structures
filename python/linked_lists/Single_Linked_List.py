class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Reference to the next node in the list

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # The head of the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If the list is empty, new node becomes head
            return
        last = self.head
        while last.next:
            last = last.next  # Traverse to the last node
        last.next = new_node  # Append the new node at the end

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next  # Remove the head node
            current = None
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:  # Data not found
            print("Data not found.")
            return
        prev.next = current.next  # Remove the node
        current = None

# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.display()  # Should display: 1 -> 2 -> 3 -> None
    sll.delete(2)
    sll.display()  # Should display: 1 -> 3 -> None
