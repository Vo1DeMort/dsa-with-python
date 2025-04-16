from collections import deque
from binaryTree import n1


def levelOrderTraversal(rootNode):
    listOfNodes = []
    traversalQueue = deque([rootNode])
    while len(traversalQueue) > 0:
        node = traversalQueue.popleft()
        listOfNodes.append(node.data)
        if node.leftChild:
            traversalQueue.append(node.leftChild)
            if node.rightChild:
                traversalQueue.append(node.rightChild)
    return listOfNodes


print(levelOrderTraversal(n1))

# TODO: i am gonna stop coding along
# and just simply try to understand the concept for now
