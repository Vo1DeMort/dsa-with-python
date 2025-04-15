# NOTE: first in fast out (FIFO)
# build in implementation, queue.Queue
# can be done with build in list, stack and linked lists

""" list based queue """


class ListQueue:
    def __init__(self):
        self.items = []
        self.front = 0  # front position
        self.rear = 0  # rear position
        self.size = 3  # size of the queue

    def enqueue(self, data):
        if self.size == self.rear:
            print('queue is full')
        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print('queu is empty')
        else:
            # delete index 0
            data = self.items.pop(0)
            # NOTE:
            # move the rest to front
            # since this is the queue with only size 3
            # if more, all the remmaining items need to be
            # moved to front
            self.rear -= 1
            return data


q = ListQueue()
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
print(q.items)

data = q.dequeue()
print(data)
print(q.items)
