# NOTE: can be done with both singly and doubly linked list

''' with doubly linked list '''


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        newNode = Node(data, None, None)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.count += 1

    def dequeue(self):
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
        elif self.count < 1:
            print('queue is empty')
        self.count -= 1
