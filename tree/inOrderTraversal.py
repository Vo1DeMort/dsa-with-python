# NOTE:
# transversing the left subtree recursively
# then right subtree
# all down and up

from binaryTree import n1


def inorder(rootNode):
    current = rootNode

    if current is None:
        return
    inorder(current.leftChild)
    print(current.data)
    inorder(current.rightChild)


inorder(n1)
