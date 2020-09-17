class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # 1) insert
    def insert(self, value):
        self.root = self._insert_value(self.root, value)
        return self.root is not None

    def _insert_value(self, node, value):
        if not node:
            node = Node(value)
        elif value <= node.value:
            node.left = self._insert_value(node.left, value)
        elif value > node.value:
            node.right = self._insert_value(node.right, value)
        return node

    # 2) search
    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.value == key:
            return root is not None
        elif key < root.value:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    # 3) delete
    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.value:
            deleted = True
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                parent, child = node, node.right
                while child.left:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.value:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted


if __name__ == "__main__":
    vals = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

    bst = BST()
    for val in vals:
        bst.insert(val)

    # Find
    print(bst.find(15))  # True
    print(bst.find(17))  # False

    # Delete
    print(bst.delete(55))  # True
    print(bst.delete(14))  # True
    print(bst.delete(11))  # False