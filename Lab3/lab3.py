class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(node):
    if node.right is not None:
        current = node.right
        while current.left is not None:
            current = current.left
        return current
    
    current = node
    while current.parent is not None and current.parent.right == current:
        current = current.parent
    return current.parent