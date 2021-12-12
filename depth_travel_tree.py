class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data


root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)


def inorder(root: Node):
    if not root:
        return
    print(root.val)
    inorder(root.left)
    inorder(root.right)


inorder(root)
