class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    # NOTE: heapify - rearranged the nodes to statisfy
    # the heap property
    def arrange(self, k):
        while k // 2 > 0:
            if self.heap[k] < self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
                k //= 2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    # NOTE: deleting the root node
    # take the last item from the list and make it the new root node
    # then reorganize the heap if that is necessary
    # moving from root node down to the last element ( percolate )

    def minChild(self, k):
        if k * 2 + 1 > self.size:
            # return index if beyond the end of the list
            return k * 2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k * 2
        else:
            return k * 2+1

    def sink(self, k):
        while k * 1 <= self.size:
            mc = self.minChild(k)
            if self.heap[k] > self.heap[mc]:
                self.heap[k], self.heap[mc] = self.heap[mc], self.heap[k]
            k = mc

    def deleteRootNode(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

    # NOTE: deleting a node
    # counting node location is left to right
    def delete(self, location):
        item = self.heap[location]
        self.heap[location] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(location)
        return item

    def heapSort(self):
        sortedList = []
        for node in range(self.size):
            n = self.deleteRootNode()
            sortedList.append(n)
        return sortedList


h = MinHeap()
unsortedList = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
for i in unsortedList:
    h.insert(i)
print(h.heap)

n = h.deleteRootNode()
print(n)
print(h.heap)

m = h.delete(2)
print(m)
print(h.heap)

print('unsorted list : {}'.format(unsortedList))
print('sorted list: {}'.format(h.heapSort()))
