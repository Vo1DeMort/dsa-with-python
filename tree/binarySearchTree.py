# NOTE: skipped few things

# NOTE:
# provide very first search ,insertion and deletion
# each node has at most two chilren
# left child < Parent None
# right child > parent node
# this applies resursively to every subtree

# NOTE: Operations
# insert, delete, find min, find max ,search

class Node:
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None


class Tree:
    def __init__(self):
        self.rootNode = None

    def insert(self, data):
        node = Node(data)
        if self.rootNode is None:
            self.rootNode = node
            return self.rootNode
        else:
            current = self.rootNode
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.leftChild
                    if current is None:
                        parent.leftChild = node
                        return self.rootNode
                else:
                    current = current.rightChild
                    if current is None:
                        parent.rightChild = node
                        return self.rootNode

    def inOrderTranversal(self, rootNode):
        current = rootNode
        if current is None:
            return
        self.inOrderTranversal(current.leftChild)
        print(current.data)
        self.inOrderTranversal(current.rightChild)

    def search(self, data):
        current = self.rootNode
        while True:
            if current is None:
                print('not found')
            elif current.data is data:
                print('fount', data)
                return data
            elif current.data > data:
                current = current.leftChild
            else:
                current = current.rightChild

    # NOTE: deletion
    # no chilren : simply remove the Node
    # one child : swap the value of the node with child
    # two children : find in-order successor or predecessor and swap the values
    # then delete
    def getNodeAndItsParent(self, data):
        parent = None
        current = self.rootNode
        if current is None:
            return (parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.leftChild
            else:
                parent = current
                current = current.rightChild
        return (parent, current)

    def delete(self, data):
        parent, node = self.getNodeAndItsParent(data)

        if parent is None and node is None:
            return False
        noOfChildren = 0

        if node.leftChild and node.rightChild:
            noOfChildren = 2
        elif (node.leftChild is None) and (node.rightChild is None):
            noOfChildren = 0
        else:
            noOfChildren = 1

        if noOfChildren == 0:
            if parent:
                if parent.rightChild is node:
                    parent.rightChild = None
                else:
                    parent.leftChild = None
            else:
                self.rootNode = None
        elif noOfChildren == 1:
            nextNode = None
            if node.leftChild:
                nextNode = node.leftChild
            else:
                nextNode = node.rightChild
            if parent:
                if parent.leftChild is node:
                    parent.leftChild = nextNode
                else:
                    parent.rightChild = nextNode
            else:
                self.rootNode = nextNode
        else:
            parentOfLeftMostNode = node
            leftMostNode = node.rightChild
            while leftMostNode.leftChild:
                parentOfLeftMostNode = leftMostNode
                leftMostNode = leftMostNode.leftChild
            node.data = leftMostNode.data

            if parentOfLeftMostNode.leftChild == leftMostNode:
                parentOfLeftMostNode.leftChild = leftMostNode.rightChild
            else:
                parentOfLeftMostNode.rightChild = leftMostNode.rightChild

    def findMin(self):
        current = self.rootNode
        while current.leftChild:
            current = current.leftChild
        return current.data

    def findMax(self):
        current = self.rootNode
        while current.rightChild:
            current = current.rightChild
        return current.data


tree = Tree()
r = tree.insert(5)
r = tree.insert(2)
r = tree.insert(7)
r = tree.insert(9)
r = tree.insert(1)

tree.search(9)
tree.delete(9)
tree.search(9)

print(tree.findMin())
print(tree.findMax())
