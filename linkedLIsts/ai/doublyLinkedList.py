class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, target_data, data):
        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node = Node(data)

                # Set new node's connections
                new_node.prev = current
                new_node.next = current.next

                # Update next node's prev if it exists
                if current.next is not None:
                    current.next.prev = new_node
                else:
                    self.tail = new_node  # Update tail if inserting at end

                # Update current node's next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"Target data {target_data} not found in the list")

    def insert_before(self, target_data, data):
        if self.head and self.head.data == target_data:
            self.prepend(data)
            return

        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node = Node(data)

                # Set new node's connections
                new_node.next = current
                new_node.prev = current.prev

                # Update previous node's next
                current.prev.next = new_node

                # Update current node's prev
                current.prev = new_node
                return
            current = current.next
        raise ValueError(f"Target data {target_data} not found in the list")

    def delete(self, data):
        if self.is_empty():
            raise ValueError("List is empty")

        # Case 1: Deleting the head node
        if self.head.data == data:
            if self.head == self.tail:  # Only one node
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return

        # Case 2: Deleting the tail node
        if self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        # Case 3: Deleting a middle node
        current = self.head
        while current is not None:
            if current.data == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return
            current = current.next

        raise ValueError(f"Data {data} not found in the list")

    def search(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def display_forward(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty list")

    def display_backward(self):
        elements = []
        current = self.tail
        while current is not None:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements) if elements else "Empty list")

    def reverse(self):
        current = self.head
        while current is not None:
            # Swap prev and next pointers
            current.prev, current.next = current.next, current.prev

            # Move to the next node (which is now prev due to swap)
            current = current.prev

        # Swap head and tail
        self.head, self.tail = self.tail, self.head


# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()

    print("Appending elements:")
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.display_forward()  # 10 <-> 20 <-> 30

    print("\nPrepending 5:")
    dll.prepend(5)
    dll.display_forward()  # 5 <-> 10 <-> 20 <-> 30

    print("\nInserting 15 after 10:")
    dll.insert_after(10, 15)
    dll.display_forward()  # 5 <-> 10 <-> 15 <-> 20 <-> 30

    print("\nInserting 25 before 30:")
    dll.insert_before(30, 25)
    dll.display_forward()  # 5 <-> 10 <-> 15 <-> 20 <-> 25 <-> 30

    print("\nDisplaying backward:")
    dll.display_backward()  # 30 <-> 25 <-> 20 <-> 15 <-> 10 <-> 5

    print("\nDeleting 20:")
    dll.delete(20)
    dll.display_forward()  # 5 <-> 10 <-> 15 <-> 25 <-> 30

    print("\nSearching for 15:", dll.search(15))  # True
    print("Searching for 99:", dll.search(99))   # False

    print("\nList size:", dll.size())  # 5

    print("\nReversing the list:")
    dll.reverse()
    dll.display_forward()  # 30 <-> 25 <-> 15 <-> 10 <-> 5
