from binaryTree import n1


def postOrder(rootNode):
    current = rootNode
    if current is None:
        return
    postOrder(current.leftChild)
    postOrder(current.rightChild)
    print(current.data)


postOrder(n1)
