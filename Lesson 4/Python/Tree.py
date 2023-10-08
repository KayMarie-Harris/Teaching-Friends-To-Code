class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)

    def insert_left(self, parent_node, data):
        new_node = TreeNode(data)
        parent_node.left = new_node

    def insert_right(self, parent_node, data):
        new_node = TreeNode(data)
        parent_node.right = new_node

    def __repr__(self):
        return self._repr_recursive(self.root)

    def _repr_recursive(self, node):
        if node is None:
            return ""
        result = str(node.data)
        if node.left or node.right:
            result += " -> ("
            if node.left:
                result += self._repr_recursive(node.left)
            result += ")"
            if node.right:
                result += " -> ("
                result += self._repr_recursive(node.right)
                result += ")"
        return result


# Example usage:
tree = BinaryTree(1)
tree.insert_left(tree.root, 2)
tree.insert_right(tree.root, 3)
tree.insert_left(tree.root.left, 4)
tree.insert_right(tree.root.left, 5)

print(tree)
