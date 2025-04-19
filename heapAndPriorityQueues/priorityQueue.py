# NOTE:
# queue ,but priority is attached with the data
# data elements with highest priotiy are retrived before
# the lower priority data elements
# if two data elements have the same priority , FIFO comes in
# can be implemented by modifying an enqueue position by inserting
# the item according to the priotity

class Node:
    def __init__(self, info, priority):
        self.info = info
        self.priority = priority


class PriorityQueue:
    ''' smallest priority or highest priority '''

    def __init__(self):
        self.queue = []

    # NOTE: insert if initail value is empty
    # if not , perform traversal and reach the appropriate
    # index
    def insert(self, node):
        if len(self.queue) == 0:
            self.queue.append(node)
        else:
            for x in range(0, len(self.queue)):
                if node.priority >= self.queue[x].priority:
                    if x == (len(self.queue)-1):
                        self.queue.insert(x+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)
                    return True

    def delete(self):
        x = self.queue.pop(0)
        print('deleted data with the given priority :', x.info, x.priority)
        return x

    def show(self):  # print entire queue
        for x in self.queue:
            print(str(x.info) + "-" + str(x.priority))


p = PriorityQueue()
p.insert(Node("cat", 13))
p.insert(Node("bat", 2))
p.insert(Node("rat", 1))
p.insert(Node("ant", 26))
p.insert(Node("lion", 25))
p.show()
p.delete()

# NOTE: Can be implemented with several data structure
# but mostly implemented with 'heap' due to efficiency


class PriorityQueueHeap:
    def __init__(self):
        self.heap = [()]

    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k][0] < self.heap[k//2][0]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k //= 2

    def insert(self, priority, item):
        self.heap.append((priority, item))
        self.size += 1
        self.arrange(self.size)

    def sink(self, k):
        while k * 2 <= self.size:
            mc = self.minchild(k)
            if self.heap[k][0] > self.heap[mc][0]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def minchild(self, k):
        if k * 2 + 1 > self.size:
            return k * 2
        elif self.heap[k*2][0] < self.heap[k*2+1][0]:
            return k*2
        else:
            return k * 2 + 1

    def deleteRootNode(self):
        item = self.heap[1][1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item


h = PriorityQueueHeap()
h.insert(2, 'bat')
h.insert(13, 'cat')
h.insert(18, 'rat')
h.insert(26, 'ant')
h.insert(3, 'lion')
h.insert(4, 'bear')

for i in range(h.size):
    n = h.deleteRootNode()
    print(n)
    print(h.heap)
