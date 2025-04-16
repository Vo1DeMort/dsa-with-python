from binaryTree import n1


def preorder(rootNode):
    current = rootNode
    if current is None:
        return
    print(current.data)
    preorder(current.leftChild)
    preorder(current.rightChild)


preorder(n1)

