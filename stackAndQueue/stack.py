# NOTE: last in fast out (lIFO)


# NOTE:
# can be implement with both array and linked list
# the one with array will have fixed size
# whereas the one with linked list will not

# NOTE:
# if the stack with array is full will generate error
# which is called overflow (stack overflow)
# trying to pop an empty stack will cause underflow


""" with array"""


size = 3
data = [0] * (size)
# size = 5
# data = [0] * size
# print(data)  # Output: [0, 0, 0, 0, 0]
top = -1


def push(x):
    global top
    if top >= size - 1:
        print('stack overflow')
    else:
        top = top+1
        data[top] = x


push('egg')
push('ham')
push('spam')
print(data[0:top+1])
push('new')


def pop():
    global top
    if top == -1:
        print("stack underflow")
    else:
        top = top-1
        data[top] = 0
        return data[top+1]


print(data[0:top+1])
pop()
pop()
pop()
pop()
pop()
print(data[0:top+1])


def peek():
    global top
    if top == -1:
        print('stack is empty')
    else:
        print(data[top])


''' with linked list'''


class Node:
    def __init__(self, data=None):
        # data of current node
        self.data = data
        # point to the node beneath the current node
        self.next = None


class Stack:
    def __init__(self):
        # top most item of the stack
        # if this has value ,the stack is not empty
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            print('stack is empty')

    def peek(self):
        if self.top:
            return self.top.data
        else:
            print('stack is empty')


words = Stack()
words.push('egg')
words.push('ham')
words.push('spam')

current = words.top
while current:
    print(current.data)
    current = current.next

words.pop()
current = words.top
while current:
    print(current.data)
    current = current.next

words.peek()
