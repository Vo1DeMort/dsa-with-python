# NOTE: max of two childre, left and right child
# Type	                   Description
# Full Binary Tree	       Every node has 0 or 2 children
# Perfect Binary Tree	   All levels are filled completely
# Complete Binary Tree	   All levels are filled, last level is filled from left
# Balanced Tree	           Left and right subtrees’ height differ by at most 1
# Binary Search Tree(BST)  Left child < node < right child

class Node:
    def __init__(self, data):
        self.data = data
        self.rightChild = None
        self.leftChild = None


n1 = Node('root node')
n2 = Node('left child node')
n3 = Node('right child node')
n4 = Node('left grandchild node')

n1.leftChild = n2
n1.rightChild = n3
n2.leftChild = n4

# traversal of left sub tree
current = n1
while current:
    print(current.data)
    current = current.leftChild

# NOTE:
# start from a node and traverse every available child node
# then to next sibling
# in-order, pre-order, post-order

# NOTE:
# start from the root node
# then visit all the nodes on each level
# process the node level by level
