class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert_left(self, current_node, value):
        if current_node.left is None:
            current_node.left = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        if current_node.right is None:
            current_node.right = TreeNode(value)
        else:
            new_node = TreeNode(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def preorder_traversal(self, node, visit):
        if node:
            visit(node)
            self.preorder_traversal(node.left, visit)
            self.preorder_traversal(node.right, visit)

    def inorder_traversal(self, node, visit):
        if node:
            self.inorder_traversal(node.left, visit)
            visit(node)
            self.inorder_traversal(node.right, visit)

    def postorder_traversal(self, node, visit):
        if node:
            self.postorder_traversal(node.left, visit)
            self.postorder_traversal(node.right, visit)
            visit(node)

    def find(self, value):
        """
        Find a node with the given value in the binary tree.
        Returns the node if found, else None.
        """

        def _find_recursive(node, value):
            if node is None:
                return None
            if node.value == value:
                return node
            left_result = _find_recursive(node.left, value)
            if left_result is not None:
                return left_result
            return _find_recursive(node.right, value)

        return _find_recursive(self.root, value)

    def visualize(self, node=None, prefix="", is_tail=True):
        """
        Visualize the binary tree structure using ASCII characters
        """
        if node is None:
            node = self.root

        if node is not None:
            print(prefix + ("└── " if is_tail else "├── ") + str(node.value))

            children = []
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)

            for i, child in enumerate(children):
                is_last = i == len(children) - 1
                extension = "    " if is_tail else "│   "
                if child == node.left:
                    self.visualize(
                        child, prefix + extension, is_last and node.right is None
                    )
                else:
                    self.visualize(child, prefix + extension, is_last)


# Example usage:
tree = BinaryTree(13)

# Inserting nodes for binary search tree
tree.insert_left(tree.root, 7)
tree.insert_right(tree.root, 15)
tree.insert_left(tree.root.left, 3)
tree.insert_right(tree.root.left, 8)
tree.insert_left(tree.root.right, 14)
tree.insert_right(tree.root.right, 19)
tree.insert_left(tree.root.right.right, 18)


def print_node(node):
    print(node.value)


print("ASCII Tree Visualization:")
tree.visualize()

# print("\nInorder Traversal:")
# tree.inorder_traversal(tree.root, print_node)

print("\nOutput of Find Method 18:")
found_node = tree.find(18)
if found_node:
    print(f"Node with value {found_node.value} found.")
else:
    print("Node not found.")

print("\nOutput of Find Method 20:")
found_node = tree.find(20)
if found_node:
    print(f"Node with value {found_node.value} found.")
else:
    print("Node not found.")
