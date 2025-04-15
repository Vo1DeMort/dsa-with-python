class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  # Points to itself
        else:
            current = self.head
            while current.next != self.head:  # Traverse until last node
                current = current.next
            current.next = new_node
            new_node.next = self.head  # Make it circular

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:  # Find last node
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node  # Update head

    def insert_after(self, target_data, data):
        if self.is_empty():
            raise ValueError("List is empty")

        new_node = Node(data)
        current = self.head

        while True:
            if current.data == target_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head:  # Completed full circle
                break
        raise ValueError(f"Target data {target_data} not found in the list")

    def delete(self, data):
        if self.is_empty():
            raise ValueError("List is empty")

        # Case 1: Deleting the head node
        if self.head.data == data:
            if self.head.next == self.head:  # Only one node
                self.head = None
            else:
                current = self.head
                while current.next != self.head:  # Find last node
                    current = current.next
                current.next = self.head.next  # Bypass head
                self.head = self.head.next  # Update head
            return

        # Case 2: Deleting other nodes
        current = self.head
        prev = None
        while True:
            if current.data == data:
                prev.next = current.next
                return
            prev = current
            current = current.next
            if current == self.head:  # Completed full circle
                break
        raise ValueError(f"Data {data} not found in the list")

    def search(self, data):
        if self.is_empty():
            return False

        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:  # Completed full circle
                break
        return False

    def size(self):
        if self.is_empty():
            return 0

        count = 0
        current = self.head
        while True:
            count += 1
            current = current.next
            if current == self.head:
                break
        return count

    def display(self):
        if self.is_empty():
            print("Empty list")
            return

        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print(" -> ".join(elements) + " -> (head)")

    def split_list(self):
        """Splits the circular list into two halves"""
        if self.is_empty() or self.head.next == self.head:
            return None, None  # Can't split single node or empty list

        slow = self.head
        fast = self.head

        # Find midpoint (slow will be at midpoint when fast completes traversal)
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        # Create second half
        head2 = slow.next
        slow.next = self.head  # Make first half circular

        # Make second half circular
        temp = head2
        while temp.next != self.head:
            temp = temp.next
        temp.next = head2

        return self.head, head2


# Example usage
if __name__ == "__main__":
    cll = CircularLinkedList()

    print("Appending elements:")
    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.display()  # 10 -> 20 -> 30 -> (head)

    print("\nPrepending 5:")
    cll.prepend(5)
    cll.display()  # 5 -> 10 -> 20 -> 30 -> (head)

    print("\nInserting 15 after 10:")
    cll.insert_after(10, 15)
    cll.display()  # 5 -> 10 -> 15 -> 20 -> 30 -> (head)

    print("\nDeleting 20:")
    cll.delete(20)
    cll.display()  # 5 -> 10 -> 15 -> 30 -> (head)

    print("\nSearching for 15:", cll.search(15))  # True
    print("Searching for 99:", cll.search(99))   # False

    print("\nList size:", cll.size())  # 4

    print("\nSplitting the list:")
    head1, head2 = cll.split_list()

    # Display first half
    print("First half:")
    current = head1
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current == head1:
            break
    print("(head)")

    # Display second half
    print("Second half:")
    current = head2
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current == head2:
            break
    print("(head)")
