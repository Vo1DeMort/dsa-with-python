
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, target_data, data):
        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"Target data {target_data} not found in the list")

    def delete(self, data):
        if self.is_empty():
            raise ValueError("List is empty")

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
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

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()

    print("Appending elements:")
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.display()  # 10 -> 20 -> 30

    print("\nPrepending 5:")
    sll.prepend(5)
    sll.display()  # 5 -> 10 -> 20 -> 30

    print("\nInserting 15 after 10:")
    sll.insert_after(10, 15)
    sll.display()  # 5 -> 10 -> 15 -> 20 -> 30

    print("\nDeleting 20:")
    sll.delete(20)
    sll.display()  # 5 -> 10 -> 15 -> 30

    print("\nSearching for 15:", sll.search(15))  # True
    print("Searching for 99:", sll.search(99))   # False

    print("\nList size:", sll.size())  # 4

    print("\nReversing the list:")
    sll.reverse()
    sll.display()  # 30 -> 15 -> 10 -> 5
