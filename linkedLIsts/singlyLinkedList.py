from node import Node


'''hold the list'''


class SinglyLinkedList:
    def __init__(self):
        # head of the list
        self.head = None
        self.tail = None
        self.size = 0

    # append at the end
    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def appendSpecific(self, data, index):
        current = self.head
        prev = self.head
        node = Node(data)
        count = 1
        while current:
            if count == 1:
                node.next = current
                self.head = node
                print(count)
                return
            elif index == index:
                node.next = current
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
        if count < index:
            print('the list has less number of elements')

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False

    def getSize(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def deleteFirst(self):
        current = self.head
        if self.head is None:
            print('no data element to delete')
        elif current == self.head:
            self.head = current.next

    def deleteLast(self):
        current = self.head
        prev = self.head
        while current:
            if current.next is None:
                prev.next = current.next
                self.size -= 1
            prev = current
            current = current.next

    def clear(self):
        self.tail = None
        self.head = None


words = SinglyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

current = words.head
while current:
    print(current.data)
    current = current.next
